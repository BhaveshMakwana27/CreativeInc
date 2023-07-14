from django.shortcuts import render,HttpResponse

def blogHome(request):
    return HttpResponse('blog home')
def blogPost(request,slug):
    return HttpResponse(f'blog post {slug}')