from django.shortcuts import render, get_object_or_404
from .models import Blog
from .templatetags import pluralize

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'pluralize': pluralize})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})

