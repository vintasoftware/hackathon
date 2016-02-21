from django import forms
from django.contrib.auth import get_user_model

from users.forms import PasswordResetForm

from groups.models import Group, Link, GroupMembership

User = get_user_model()


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name',)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self):
        group = super().save()
        GroupMembership.objects.create(group=group, user=self.user,
                                       is_creator=True, is_admin=True)
        return group


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('url',)


class AddUserGroupForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, request, group, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.request = request
            self.group = group

    def save(self):
        email = self.cleaned_data['email']
        user, created = User.objects.get_or_create(
            email=email)
        if created:
            reset_form = PasswordResetForm({'email': email})
            assert reset_form.is_valid()
            reset_form.save(request=self.request,
                            email_template_name='users/emails/password_reset_email.html')
        return GroupMembership.objects.create(group=self.group, user=user)
