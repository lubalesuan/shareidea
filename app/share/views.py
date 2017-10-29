from django.shortcuts import get_object_or_404, render
from .models import Project, CustomUser, Categories
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
	template_name = 'share/index.html'
	def get_queryset(self):
		return Project.objects.filter(
			publish_date__lte = timezone.now()
		).order_by('-publish_date')

	
