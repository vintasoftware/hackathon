from django import forms

from groups.models import Group, Link


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('url',)
