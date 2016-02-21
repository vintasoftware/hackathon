from django.conf.urls import url, include

from .views import UserLoginView, UserLogoutView, UserCreateView, PasswordResetView

urlpatterns = [
    url(r'^login/', UserLoginView.as_view(), name='login'),
    url(r'^logout/', UserLogoutView.as_view(), name='logout'),
    url(r'^create/', UserCreateView.as_view(), name='create'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetView.as_view(), name='password_reset_confirm'),
    # url(r'^', include('authtools.urls')),
]
