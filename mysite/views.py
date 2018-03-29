from django.http import HttpResponse 
from django.shortcuts import  render
from django.views.generic import TemplateView
import datetime

class hello(TemplateView):
  template_name = 'base_page.html'
 


