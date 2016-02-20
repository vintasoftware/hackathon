from django.conf.urls import url, include

from .views import UserLoginView, UserLogoutView, UserCreateView

urlpatterns = [
    url(r'login/', UserLoginView.as_view(), name='login'),
    url(r'logout/', UserLogoutView.as_view(), name='logout'),
    url(r'create/', UserCreateView.as_view(), name='create'),
    # url(r'^', include('authtools.urls')),
]
