from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='project_list'),
    url(r'^create/', views.createProject,name='project_create'),
]