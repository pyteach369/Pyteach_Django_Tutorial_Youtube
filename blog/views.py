from django.shortcuts import render
from django.views import generic

from .models import Post


class PostListView(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status='pub')
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    ordering = ['title',]

    paginate_by = 3
