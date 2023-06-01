from django import forms
from django.forms import ModelForm

from articleapp.models import Articles

class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editalbe', 'style': 'height: auto;'}))
    
    class Meta:
        model = Articles
        fields =['title', 'image', 'project', 'content']