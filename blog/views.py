from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView
from . models import Post 

class BlogView(ListView):
    model  = Post
    template_name  =  'blogintro.html'

class DetailBlogView(DetailView):
    model  =  Post 
    template_name = 'detail_blog.html'