from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from anvil.views import protected_resource

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template':'index.html'}, name="index_page"),
    url(r'^protected/$', protected_resource, name="protected_page"),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login_page"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name="logout_page")
)
