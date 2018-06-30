from blog.models import Submission
from django import forms
class SubmissionForm(forms.ModelForm):

    class Meta :
        model = Submission
        fields = ['text', ]
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control' , 'placeholder':'your code here' ,'cols': 10, 'rows': 18,}),

        }
        labels = {
            'text':"Paste your code" ,
        }


