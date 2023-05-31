from django.forms import ModelForm

from articleapp.models import Articles

class ArticleCreationForm(ModelForm):
    class Meta:
        model = Articles
        fields =['title', 'image', 'project', 'content']