from authtools.forms import UserCreationForm

from django.contrib.auth.forms import PasswordResetForm

from .models import User


CreateUserForm = UserCreationForm


class PasswordResetForm(PasswordResetForm):
    def get_users(self, email):
        users = User.objects.filter(
            email__iexact=email)
        return (u for u in users)
