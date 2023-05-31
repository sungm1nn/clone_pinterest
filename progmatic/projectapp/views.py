from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from articleapp.models import Articles
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import MultipleObjectMixin
# Create your views here.
@method_decorator(login_required, 'post')
@method_decorator(login_required, 'get')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'
    
    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk':self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    
    paginate_by = 25
    
    def get_context_data(self, **kwargs: Any):
        object_list = Articles.objects.filter(project=self.get_object())
        return super(ProjectDetailView,self).get_context_data(object_list=object_list,**kwargs)
    
class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25