from django.conf.urls import url

from groups.views import ListGroups, ListLinks, GroupCreate, LinkCreate

urlpatterns = [
    url(r'^groups/$', ListGroups.as_view(), name='list_groups'),
    url(r'^groups/(?P<group_id>[0-9]+)/links/$', ListLinks.as_view(), name='list_links'),
    url(r'^groups/create/$', GroupCreate.as_view(), name='create_group'),
    url(r'^groups/(?P<group_id>[0-9]+)/links/create/$', LinkCreate.as_view(), name='create_link'),
]
