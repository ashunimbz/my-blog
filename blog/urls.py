from django.conf.urls import url
from django.contrib import admin
from mysite.views import hello
from . import views



urlpatterns = [
    url(r'^$' , views.BlogView.as_view() , name = 'blog_url' ) , 
   url(r'^post/(?P<pk>[0-9]+)/$' ,views.DetailBlogView.as_view() , name =  'post_detail' ),
    url(r'^submit$',views.submit, name = 'blog_submit')
]
