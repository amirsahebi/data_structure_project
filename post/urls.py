from django.contrib.auth import login
from django.urls import path
from django.urls.resolvers import URLPattern

from post.forms import PostModelForm
from .views import AddPost,DeletePost,EditPost

from .views import PostDetailView,PostListView

urlpatterns = [
    path('<slug:slug>',PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
    path('create_post/', AddPost, name="post_form"),
    path('edit-post/<slug:slug>',EditPost,name="edit-post-form"),
    path('delete-post/<slug:slug>',DeletePost,name="delete-post"),
]
