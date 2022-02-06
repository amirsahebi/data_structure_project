from django.db import models
from django.urls import reverse
from uuslug import slugify
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=55)
    image = models.ImageField()
    barcode = models.PositiveIntegerField(unique=True,null=False)
    cost = models.PositiveIntegerField()
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False,unique=True)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.name = slugify(self.name, self)
        super(Post, self).save(*args, **kwargs)



class Price(models.Model):
    product = models.ForeignKey(Post,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()