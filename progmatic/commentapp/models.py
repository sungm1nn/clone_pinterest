from django.db import models
from django.contrib.auth.models import User
from articleapp.models import Articles

# Create your models here.
class Comment(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, related_name='comment')
    
    content = models.TextField(null=False)
    create_at = models.DateField(auto_now=True)
    