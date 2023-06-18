from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('blogComment', views.blogComment, name='blogComment'),
    path('<str:slug>', views.blogPost, name='blogPost')
]