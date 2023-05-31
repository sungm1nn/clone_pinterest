from django.shortcuts import render
from django.urls import reverse
from articleapp.models import Articles
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment
from django.views.generic import CreateView, DeleteView
from django.utils.decorators import method_decorator
# Create your views here.
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'
    
    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Articles.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})

@method_decorator(comment_ownership_required,'get')
@method_decorator(comment_ownership_required,'post')
class CommentdeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'
    
    def get_success_url(self) -> str:
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})