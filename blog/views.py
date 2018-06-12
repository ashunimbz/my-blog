from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView
from . models import Post , PostForm
from django.http import HttpResponse

class BlogView(ListView):
    model  = Post
    template_name  =  'blogintro.html'

class DetailBlogView(DetailView):
    model  =  Post 
    template_name = 'detail_blog.html'

def submit(request):
    if request.method == 'POST':

        form  = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.verified = False
            obj.save()
        return render(request , 'aftersubmit.html',{})


    else :
        form = PostForm()
        return render(request   , 'submit.html' , {'form' : form})