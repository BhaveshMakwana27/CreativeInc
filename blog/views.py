from django.shortcuts import render,HttpResponse
from .models import Post

def blogHome(request):
    allPosts = Post.objects.all()
    return render(request,'blog/bloghome.html',{'allPosts':allPosts})

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    return render(request,'blog/blogpost.html',{'post':post})