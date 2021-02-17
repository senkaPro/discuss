from django.shortcuts import get_object_or_404,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import widgets
from django.urls.base import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django import forms
from django.views.generic import CreateView,DetailView,ListView,DeleteView
from .models import Link
from .forms import LinkForm

class LinkCreateView(CreateView):
    template_name = 'link_create.html'
    form_class = LinkForm
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LinkCreateView, self).dispatch(request=request, *args, **kwargs)

    def form_valid(self, form):
        link = form.save(commit=False)
        link.submitted_by = self.request.user
        link.save()
        self.object = link
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('link-detail', kwargs={'pk':self.object.pk})

class LinkDetail(DetailView):
    template_name = 'link_detail.html'
    model = Link

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LinkDetail, self).dispatch( *args, **kwargs)

class LinkList(ListView):
    template_name = 'link_list.html'
    model = Link
    paginate_by = 3
    queryset = Link.objects.all()
    ordering = ['-submitted_on']


    def get_context_data(self, **kwargs):
        context = super(LinkList, self).get_context_data()
        qs = self.get_queryset()
        self.object_list = qs.filter(submitted_by=self.request.user)
        context['object_list'] = self.object_list
        return context

class LinkDelete(DeleteView):
    template_name = 'link_delete.html'

    @method_decorator(login_required)
    def dispatch(self, request,  *args, **kwargs):
        return super(LinkDelete,self).dispatch(request=request, *args, **kwargs)
        
    def get_success_url(self):
        return HttpResponseRedirect(reverse_lazy('user-links')) 
    

    def get_object(self, queryset=None):
        _id = self.kwargs.get('pk')
        obj = get_object_or_404(Link, pk=_id)
        if obj is None:
            return HttpResponseRedirect(reverse_lazy('home'))
        return obj

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        return render(request, 'link_delete.html', {'object':object})
    
    
