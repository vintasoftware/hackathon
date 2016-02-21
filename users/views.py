from django.core.urlresolvers import reverse
from django.views import generic

from authtools.views import LoginView, LogoutView

from .forms import CreateUserForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):

    def get_redirect_url(self):
        return reverse('users:login')


class UserCreateView(generic.CreateView):
    form_class = CreateUserForm
    template_name = 'users/create.html'

    def get_success_url(self):
        return reverse('groups:list_groups')
