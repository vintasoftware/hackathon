from django.views import generic

from .models import Group, Link


class Home(generic.TemplateView):
    template_name = 'landing_page.html'


class ListGroups(generic.ListView):
    model = Group
    template_name = 'groups_list.html'


class ListLinks(generic.ListView):
    template_name = 'links_list.html'

    def get_queryset(self):
        return Link.objects.filter(group_id=self.kwargs['group_id'])

home = Home.as_view()
list_groups = ListGroups.as_view()
list_links = ListLinks.as_view()
