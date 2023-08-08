from typing import Any, Dict
from django.shortcuts import render
from .models import Post
from django.views import View


class BlogHome(View):
    def get(self, request):
        context = {
            'posts' : Post.objects.all(),
            'title' : 'Blog',
        }
        return render(request, 'blog/blog-home.html', context)



def about(request):
    return render(request, 'blog/blog-about.html', {'title' : 'About'})

