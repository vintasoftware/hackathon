from django.shortcuts import get_object_or_404

from braces.views import LoginRequiredMixin, UserPassesTestMixin

from .models import Group, Link


class UserInGroupMixin(LoginRequiredMixin, UserPassesTestMixin):
    raise_exception = True

    def test_func(self, user):
        group = get_object_or_404(Group, pk=self.kwargs['group_id'])
        return group in user.group_set.all()


class UserLinkMixin(LoginRequiredMixin, UserPassesTestMixin):
    raise_exception = True

    def test_func(self, user):
        link = get_object_or_404(Link, pk=self.kwargs['pk'])
        return link.group in user.group_set.all()
