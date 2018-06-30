from blog.models import Submission
from django import forms


lang_choices = [
    ('C','C'),
    ('C++','C++'),
    ('Java','Java'),
    ('Python3','Python3'),
]
class SubmissionForm(forms.ModelForm):
    language = forms.ChoiceField(choices=lang_choices,widget=forms.Select(attrs={'class':'form-control'}))
    class Meta :
        model = Submission
        fields = ['text','language']
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control' , 'placeholder':'your code here,If using java name your class as "Main"' ,'cols': 10, 'rows': 18}),
        }
        labels = {
            'text':"Paste your code" ,
        }


