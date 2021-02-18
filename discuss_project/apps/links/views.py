from django.shortcuts import get_object_or_404,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import widgets
from django.urls.base import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django import forms
from django.views.generic import CreateView,DetailView,ListView,DeleteView
from django.views.generic.edit import UpdateView
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


class LinkEdit(UpdateView):
    template_name = 'link_edit.html'
    model = Link
    form_class = LinkForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(Link, pk=kwargs.get('pk'))
        if obj.submitted_by != request.user:
            return HttpResponseRedirect(reverse('home'))
        return super(LinkEdit, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('link-detail', kwargs={'pk':self.object.pk})

class LinkDetail(DetailView):
    template_name = 'link_detail.html'
    model = Link

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        obj = get_object_or_404(Link, pk=kwargs.get('pk'))
        if obj.submitted_by != self.request.user:
            return HttpResponseRedirect(reverse('home'))
        return super(LinkDetail, self).dispatch(*args, **kwargs)

class LinkList(ListView):
    template_name = 'link_list.html'
    model = Link
    paginate_by = 3
    ordering = ['-submitted_on']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        print()

        if str(self.request.user) != str(kwargs.get('user')):
            return HttpResponseRedirect(reverse('home'))
        return super(LinkList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        super(LinkList, self).get_queryset(**kwargs)
        return Link.objects.filter(submitted_by=self.request.user)

class LinkDelete(DeleteView):
    template_name = 'link_delete.html'
    model = Link

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(Link, pk=kwargs.get('pk'))
        if obj.submitted_by != request.user:
            return HttpResponseRedirect(reverse('home'))
        return super(LinkDelete, self).dispatch(request, *args, **kwargs)
        
    def get_success_url(self):
        user = self.request.user
        return reverse_lazy('user-links', kwargs={'user':user})
    

    def get_object(self, queryset=None):
        _id = self.kwargs.get('pk')
        object = get_object_or_404(Link, pk=_id)
        user = self.request.user
        if object is None:
            return HttpResponseRedirect(reverse_lazy('user-links', kwargs={'user':user}))
        return object

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        return render(request, 'link_delete.html', {'object':object})
    
    
