from __future__ import unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'authenticate', views.UserAuthentication.as_view(), name='authenticate'),  # noqa
    url(r'register', views.UserRegistration.as_view(), name='register'),
]
