from django.shortcuts import render
from django.views import generic

from .models import Post


class PostListView(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status='pub')
    ordering = ['title',]

    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    paginate_by = 6
    paginate_orphans = 1

    extra_context = {'site': 'pyteach.ir'}
    page_kwarg = 'p'


class PostDetailView(generic.DetailView):
    # model = Post
    queryset = Post.objects.filter(status='pub')
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    pk_url_kwarg = 'id'
    # slug_url_kwarg = 'javad'
    # query_pk_and_slug = True
    
    # slug_field = 'code'
    

    extra_context = {'site': 'pyteach.ir'}
