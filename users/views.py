from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.views import generic

from authtools.views import LoginView, LogoutView, PasswordResetConfirmAndLoginView


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
        login(self.request, self.object)
        return reverse('groups:list_groups')


class PasswordResetView(PasswordResetConfirmAndLoginView):
    template_name = 'users/password_reset_confirm.html'
