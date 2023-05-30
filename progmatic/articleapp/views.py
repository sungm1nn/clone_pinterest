from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Articles
from articleapp.decorators import article_ownership_required

# Create your views here.
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreationView(CreateView):
    model = Articles
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'
    
    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})
    
class ArticleDetailView(DetailView):
    model = Articles
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'
    
@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Articles
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})
    
class ArticelsDeleteView(DeleteView):
    model = Articles
    context_object_name = 'target_article'
    template_name ='articleapp/delete.html'
    success_url = reverse_lazy('articleapp:list')
    
class ArticeListView(ListView):
    model = Articles
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 25
    