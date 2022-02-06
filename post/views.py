from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.views import View
# Create your views here.
from .models import Post, Price
from .forms import PostDeleteModelForm, PostModelForm, PostModelFormView


class PostListView(View):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'products_list.html', {'posts': posts})

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('from-price') and self.request.POST.get('until-price'):
            frome=self.request.POST.get('from-price')
            until=self.request.POST.get('until-price')
            posts = Post.objects.all()
            answers = []
            for post in posts:
                if post.cost>=int(frome) and post.cost<=int(until):
                    answers.append(post)
            return render(request, 'products_list.html', {'posts': answers})


class PostDetailView(View):
    model = Post
    template_name = 'post_detail.html'
    
    def get(self, request, *args, **kwargs):
        self.post = self.model.objects.get(slug=self.kwargs['slug'])
        self.costs = Price.objects.filter(product = self.post)
        print(self.costs)
        self.icosts = []
        for cost in self.costs:
            self.icosts += [cost.value]
        # calculate the middle cost
        print(self.icosts)
        mergeSort(self.icosts)
        if len(self.icosts)%2 == 0:
            self.middle_cost = (self.icosts[len(self.icosts)//2] + self.icosts[(len(self.icosts)//2)-1])/2 
        else:
            self.middle_cost = self.icosts[(len(self.icosts)-1)//2]
        # calculate more expensive products
        self.expensives = self.model.objects.filter(cost__gt=self.post.cost)
        print(self.expensives)
        # calculate cheaper products
        self.cheapers = self.model.objects.filter(cost__lt=self.post.cost)
        print(self.cheapers)
        return render(request, 'post_detail.html',{'post':self.post,'middle_cost':self.middle_cost,'expensives':self.expensives,'cheapers':self.cheapers})
    

def mergeSort(arr):
        if len(arr) > 1:
    
            # Finding the mid of the array
            mid = len(arr)//2
    
            # Dividing the array elements
            L = arr[:mid]
    
            # into 2 halves
            R = arr[mid:]
    
            # Sorting the first half
            mergeSort(L)
    
            # Sorting the second half
            mergeSort(R)
    
            i = j = k = 0
    
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
    
            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

def AddPost(request):
    form = PostModelForm()
    if request.method == "POST":
        form = PostModelForm(request.POST,request.FILES)
        print("----------")
        if form.is_valid():
            print("+++++++++")
            updated_request = request.POST.copy()
            updated_request.update({'slug': 'a'})
            form = PostModelFormView(updated_request,request.FILES)
            a=form.save()
            a.slug = a.name
            a.save()
            b = Price(product = a,value = a.cost)
            b.save()
            messages.add_message(request, messages.ERROR, f'The post successfully saved!',extra_tags="success")
            return redirect(reverse('post_list'))

    return render(request,'forms/post_form.html',{'form':form})


def EditPost(request,slug):
    post = get_object_or_404(Post,slug=slug)
    form = PostModelForm(instance=post)

    if request.method == "POST":
        form =PostModelForm(request.POST,instance=post) 
        if form.is_valid():
            a=form.save()
            b = Price(product = a,value = a.cost)
            b.save()
            return redirect(reverse('post_list'))

    return render(request,'forms/edit_post_form.html',{'form':form,'post':post})

    


def DeletePost(request,slug):
    
    post = get_object_or_404(Post,slug=slug)
    
    form = PostDeleteModelForm(instance=post)
    if request.method == "POST":
        post.delete()
        return redirect('/') 


    return render(request,'forms/delete_post_form.html',{'form':form,'post':post})
    

