from authtools.forms import UserCreationForm

from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm

from .models import User


class CreateUserForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=commit)
        user = authenticate(email=user.email, password=self.cleaned_data['password1'])
        return user


class PasswordResetForm(PasswordResetForm):
    def get_users(self, email):
        users = User.objects.filter(
            email__iexact=email)
        return (u for u in users)
