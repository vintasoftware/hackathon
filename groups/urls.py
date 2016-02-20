from django.conf.urls import url


urlpatterns = [
    url(r'^groups/$', 'groups.views.list_groups', name='list_groups'),
    url(r'^groups/(?P<group_id>[0-9]+)/links/$', 'groups.views.list_links', name='list_links'),
]
