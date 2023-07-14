from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='Homepage'),
    path('contact/',views.contactUs,name='ContactUs'),
    path('about/',views.aboutUs,name='AboutUs')
]