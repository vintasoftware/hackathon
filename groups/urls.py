from django.conf.urls import url

from groups.views import (
    ListGroups, ListLinks, GroupCreate, LinkCreate, LinkDetail,
    AddUserGroupView)

urlpatterns = [
    url(r'^groups/$', ListGroups.as_view(), name='list_groups'),
    url(r'^groups/(?P<group_id>[0-9]+)/links/$', ListLinks.as_view(), name='list_links'),
    url(r'^groups/create/$', GroupCreate.as_view(), name='create_group'),
    url(r'^groups/(?P<group_id>[0-9]+)/links/create/$', LinkCreate.as_view(), name='create_link'),
    url(r'^groups/(?P<group_id>[0-9]+)/add_user/$', AddUserGroupView.as_view(), name='add_user_to_group'),
    url(r'link/(?P<pk>\d+)/$', LinkDetail.as_view(), name='link_detail')
]
