from django.shortcuts import render,redirect
from .models import Post,BlogComment
from django.contrib import messages
from blog.templatetags import getDict

def blogHome(request):
    allPosts = Post.objects.all()
    return render(request,'blog/bloghome.html',{'allPosts':allPosts})

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    post.views+=1
    post.save()
    comments = BlogComment.objects.filter(post=post,parent=None).reverse()
    replies = BlogComment.objects.filter(post=post).exclude(parent=None).reverse()
    repliesDict = {}
    for reply in replies:
        if reply.parent.sno not in repliesDict.keys():
            repliesDict[reply.parent.sno] = [reply]
        else:
            repliesDict[reply.parent.sno].append(reply)

    countComm = len(comments)
    context = {'post':post,'comments':comments,'countComments':countComm,'replies':repliesDict}
    return render(request,'blog/blogpost.html',context)

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')

        if parentSno=='':
            comm = BlogComment(comment=comment,user=user,post=post)
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comm = BlogComment(comment=comment,user=user,post=post,parent=parent)
            messages.success(request,"reply")


        if len(comment)<=0:
            return redirect(f'/blog/{post.slug}')
        comm.save()
        return redirect(f'/blog/{post.slug}')
