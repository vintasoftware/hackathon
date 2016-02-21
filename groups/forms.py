from django import forms

from groups.models import Group, Link, GroupMembership


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
