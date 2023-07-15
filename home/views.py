from django.shortcuts import render,HttpResponse, redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    return render(request,'home/home.html')

def contactUs(request):
    if(request.method=='POST'):
        name = request.POST.get('name','')
        phone = request.POST.get('phoneNo','')
        email = request.POST.get('emailId','')
        issue = request.POST.get('issue','')

        contactus = Contact(name=name,phoneNo=phone,email=email,issue=issue)
        contactus.save()
        messages.success(request, "Your issue is submitted, we will contact you soon for that...")
        

    return render(request,'home/contactUs.html')

def aboutUs(request):
    return render(request,'home/aboutUs.html')

def search(request):
    query = request.GET.get('searchQuery')
    if len(query)<=0 or len(query)>70:
        allPosts = []
    else:
        qTitle = Post.objects.filter(title__icontains=query)
        qContent = Post.objects.filter(content__icontains=query)
        qAuthor = Post.objects.filter(author__icontains=query)
        qTimeStamp = Post.objects.filter(timeStamp__icontains=query)
    
        allPosts = qTitle.union(qContent,qAuthor,qTimeStamp)

    return render(request,'home/search.html',{'allPosts':allPosts,'query':query})

def handleSignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        emailId = request.POST['emailId']
        choosePassword = request.POST['choosePassword']
        confirmPassword = request.POST['confirmPassword']

        # validating username
        if len(username)>15 or len(username)<4:
            messages.error(request,'Username should contain no of character between 4 to 15 only')
            return redirect('/signup/')
        if not username.isalnum():
            messages.error(request,'Username must contain only alphanumeric value (a-z,0-9)')
            return redirect('/signup/')
        if not username.islower():
            messages.error(request,'Username must contain lowercase value')
            return redirect('/signup/')
        
        # validating username
        if choosePassword==confirmPassword:
            if len(choosePassword) < 8:
                messages.error(request,"Password must contain atleast 8 characters.")
                return redirect('/signup/')
        else: 
            messages.error(request,"Password doesn't match.")
            return redirect('/signup/')



        myuser = User.objects.create_user(username, emailId, choosePassword)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Your Account is created successfully')
        return redirect('/')
    else:
        pass
    return render(request,'home/signup.html')

def handleLogin(request):
    return render(request,'home/login.html')

def handleLogout(request):
    return render(request,'home/login.html')