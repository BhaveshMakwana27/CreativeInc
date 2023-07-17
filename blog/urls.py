from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    # API to post a comment
    path('postComment',views.postComment,name='PostComment'),
    path('',views.blogHome,name='BlogHome'),
    path('<str:slug>',views.blogPost,name='BlogPost'),

]