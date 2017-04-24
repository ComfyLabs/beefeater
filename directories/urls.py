from __future__ import unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'register', views.TenantRegistration.as_view(), name='register'),
]
