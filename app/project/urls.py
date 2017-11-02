from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createproject/', views.createProject,name='createproject'),
    url(r'^about/', views.about, name = 'about')
]