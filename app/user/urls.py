from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^$', views.index, name='userlist'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL }, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]