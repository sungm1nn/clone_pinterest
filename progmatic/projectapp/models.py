from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20, null=False)
    description = models.TextField(max_length=200, null = True)
    image = models.ImageField(upload_to='project/', null=False)
    create_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.pk} : {self.title}'