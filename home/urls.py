from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='Homepage'),
    path('contact/',views.contactUs,name='ContactUs'),
    path('about/',views.aboutUs,name='AboutUs'),
    path('search/',views.search,name='Search'),
    path('signup/',views.handleSignUp,name='SignUp'),
    path('login/',views.handleLogin,name='Login'),
    path('logout/',views.handleLogout,name='Logout')
]