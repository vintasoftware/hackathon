from readability import ParserClient

from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Q, Count
from django.http import JsonResponse

from braces.views import LoginRequiredMixin, UserPassesTestMixin

from .forms import GroupForm, LinkForm, AddUserGroupForm, FilterLinkForm
from .models import Group, Link
from .concepts import extract_tags
from .mixins import UserInGroupMixin, UserLinkMixin


class Home(generic.TemplateView):
    template_name = 'landing_page.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('groups:list_groups')
        return super(Home, self).get(request, *args, **kwargs)


class ListGroups(LoginRequiredMixin, generic.ListView):
    model = Group
    template_name = 'groups_list.html'

    def get_context_data(self, **kwargs):
        context = super(ListGroups, self).get_context_data(**kwargs)
        context['form'] = GroupForm(self.request.user)
        return context

    def get_queryset(self):
        return self.request.user.group_set.all()


class ListLinks(UserInGroupMixin, generic.ListView):
    template_name = 'links_list.html'
    raise_exception = True

    def test_func(self, user):
        group = get_object_or_404(Group, pk=self.kwargs['group_id'])
        return group in user.group_set.all()

    def get_context_data(self, **kwargs):
        context = super(ListLinks, self).get_context_data(**kwargs)
        context['form'] = LinkForm()
        context['filter_link_Form'] = FilterLinkForm()
        context['group'] = self.group
        context['add_user_form'] = AddUserGroupForm(self.request, self.group)
        context['tag_name'] = self.request.GET.get('tag', '')
        return context

    def get_queryset(self):
        self.group = get_object_or_404(Group, pk=self.kwargs['group_id'])
        queryset = Link.objects.filter(group=self.group)
        form = FilterLinkForm(self.request.GET)
        if form.is_valid():
            words = form.cleaned_data['content'].split()
            q_filters = Q()
            for word in words:
                q_filters |= Q(title__contains=word)
                q_filters |= Q(content__contains=word)
            queryset = queryset.filter(q_filters)
        elif self.request.GET.get('tag'):
            tag_name = self.request.GET.get('tag')
            queryset = queryset.filter(tags__name=tag_name)
        return queryset.annotate(num_votes=Count('votes')).order_by('-num_votes')


class GroupCreate(LoginRequiredMixin, generic.View):
    raise_exception = True

    def post(self, request, *args, **kwargs):
        form = GroupForm(request.user, request.POST)
        if form.is_valid():
            form.save()
        return redirect('groups:list_groups')


class LinkCreate(UserInGroupMixin, generic.View):
    raise_exception = True

    def post(self, request, *args, **kwargs):
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.group = Group.objects.get(pk=self.kwargs['group_id'])
            # extract data from readability
            parser_client = ParserClient(token=settings.READABILITY_TOKEN)
            parser_response = parser_client.get_article(link.url)
            article = parser_response.json()
            link.title = article.get('title', '')
            link.content = article.get('content', '')
            link.description = article.get('excerpt', '')
            link.save()
            tags = extract_tags(link.title + ' ' + link.content)
            link.tags.add(*tags)
        url = reverse('groups:list_links', kwargs={'group_id': self.kwargs['group_id']})
        return redirect(url)


class LinkDetail(generic.DetailView):

    model = Link


class LinkLike(UserLinkMixin, generic.View):

    def post(self, request, *args, **kwargs):
        link = get_object_or_404(Link, pk=kwargs.get('pk'))
        link.votes.add(request.user)
        return JsonResponse({'id': link.pk, 'votes': link.votes.count()})


class AddUserGroupView(UserInGroupMixin, generic.View):
    def post(self, request, *args, **kwargs):
        group = Group.objects.get(pk=kwargs['group_id'])
        # TODO add permission ( only admins)
        form = AddUserGroupForm(request, group, request.POST)
        if form.is_valid():
            try:
                created = form.save()
            except IntegrityError:
                message = 'The user is already in the group!'
                extra_tags = 'alert-warning'
            else:
                if created:
                    message = 'The user received an invitation email to access the group!'
                    extra_tags = 'alert-info'
                else:
                    message = 'The user was added to the group!'
                    extra_tags = 'alert-success'
            messages.add_message(request, messages.INFO, message, extra_tags=extra_tags)
        url = reverse('groups:list_links', kwargs={'group_id': self.kwargs['group_id']})
        return redirect(url)
