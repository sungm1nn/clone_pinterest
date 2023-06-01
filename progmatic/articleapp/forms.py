from django.forms import ModelForm
from django import forms

from articleapp.models import Articles
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-start',
                                                           'style': 'height: auto;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Articles
        fields = ['title', 'image', 'project', 'content']