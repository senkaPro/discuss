from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from django.core.paginator import Paginator
from django.conf import settings
from django.urls.base import reverse
from .forms import UserForm,UserLoginForm
from apps.links.models import Link

class HomeView(TemplateView):
    template_name = 'base.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        links = Link.objects.all().order_by('-submitted_on')
        p = Paginator(links, 3)
        page_num = self.request.GET.get('page')
        page_obj = p.get_page(page_num)
        context['page_obj'] = page_obj
        return context


class UserRegister(CreateView):
    template_name = 'register.html'
    form_class = UserForm
    model = User

    def get_success_url(self):
        return reverse('login')

class UserLogin(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True
    success_url = settings.LOGIN_REDIRECT_URL


class UserLogout(LogoutView):
    pass