from readability import ParserClient

from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings

from .forms import GroupForm, LinkForm
from .models import Group, Link


class Home(generic.TemplateView):
    template_name = 'landing_page.html'


class ListGroups(generic.ListView):
    model = Group
    template_name = 'groups_list.html'

    def get_context_data(self, **kwargs):
        context = super(ListGroups, self).get_context_data(**kwargs)
        context['form'] = GroupForm()
        return context


class ListLinks(generic.ListView):
    template_name = 'links_list.html'

    def get_context_data(self, **kwargs):
        context = super(ListLinks, self).get_context_data(**kwargs)
        context['form'] = LinkForm()
        context['group'] = self.group
        return context

    def get_queryset(self):
        self.group = get_object_or_404(Group, pk=self.kwargs['group_id'])
        return Link.objects.filter(group=self.group)


class GroupCreate(generic.View):

    def post(self, request, *args, **kwargs):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('groups:list_groups')


class LinkCreate(generic.View):

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
            link.save()
        url = reverse('groups:list_links', kwargs={'group_id':self.kwargs['group_id']})
        return redirect(url)


class LinkDetail(generic.DetailView):

    model = Link