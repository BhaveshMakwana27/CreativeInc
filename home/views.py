from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse('Home')

def contactUs(request):
    return HttpResponse('Contact')

def aboutUs(request):
    return HttpResponse('About Us')