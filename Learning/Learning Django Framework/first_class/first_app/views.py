from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
#logical kaj kora hoi
# Viws 2 types
# 1.Functional views
# 2.Class views

""" def home(request):
    return HttpResponse("<h1>This is my first response</h1>") """

def home(request):
    blogs = Blog.objects.all()
    print(blogs)
    return render(request,'home.html', {'blogs' : blogs})