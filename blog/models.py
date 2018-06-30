from django.db import models
from django.utils import timezone
from django import forms


class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    desc =  models.CharField(max_length = 500)
    verified =  models.BooleanField()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ('author' , 'title'  , 'text' ,'created_date' ,'desc' ,)
        labels = {
            'desc': "Description" ,
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'created_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {

            'author':'Enter your name',
            'desc' : 'Write a short description about your article',
            'title': 'Topic of your article',
            'text' :'Your article no more than 300 words',
        }

class Submission(models.Model):
    text  =  models.CharField(max_length=10000)

    def __str__(self):
        return self.text