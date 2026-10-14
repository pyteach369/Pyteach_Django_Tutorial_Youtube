from django.shortcuts import render
from django.views import generic

from .models import Post


class PostListView(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status='pub')
    ordering = ['title',]

    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    paginate_by = 2
    paginate_orphans = 1

    extra_context = {'site': 'pyteach.ir'}
    page_kwarg = 'p'
