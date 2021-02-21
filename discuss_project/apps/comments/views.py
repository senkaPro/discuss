from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView,ListView
from django.utils.decorators import method_decorator
from django.urls.base import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comment
from apps.links.models import Link


class CommentCreateView(CreateView):
    template_name = 'comment_form.html'
    form_class = CommentForm
    model = Comment
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.form_class.is_valid:
            pk = self.request.GET.get('link_pk')
            return HttpResponseRedirect(reverse('link-detail',kwargs={'pk':pk}))
        return super(CommentCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        link = Link.objects.get(pk=form.cleaned_data.get('link_pk'))
        comment = form.save(commit=False)
        comment.commented_by = self.request.user
        comment.commented_to = link
        comment.save()
        return HttpResponseRedirect(reverse('link-detail',kwargs={'pk':link.pk}))

    def get_initial(self):
        initial_data = super(CommentCreateView, self).get_initial()
        initial_data['link_pk'] = self.request.GET.get('link_pk')

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        link = Link.objects.get(pk=self.request.GET.get('link_pk'))
        context['link'] = link
        return context
        
   


