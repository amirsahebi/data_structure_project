from django import forms
from django.contrib.auth.models import User
from django.forms import fields

from post.models import Post, Price


class PostModelForm(forms.ModelForm):

    class Meta : 
        model = Post
        fields = ['name','image','caption','cost','barcode']

class PostModelFormView(forms.ModelForm):

    class Meta : 
        model = Post
        fields = "__all__"

class PostDeleteModelForm(forms.ModelForm):
    class Meta : 
        model = Post
        fields = []

