from django.shortcuts import render, get_object_or_404
from .models import Category, Post, Tag

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_posts(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category=category).select_related('author', 'category')
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})

def tag_posts(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    posts = Post.objects.filter(tags=tag).select_related('author', 'category')
    return render(request, 'blog/tag_posts.html', {'tag': tag, 'posts': posts})