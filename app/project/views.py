from django.shortcuts import get_object_or_404, render,redirect
from .models import Project, Category
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime

from .forms import SearchForm, CreateProjectForm

def index(request):
	print('in index')
	results = Project.objects.all()

	if request.method == 'POST':
		print('post')
		name = request.POST.get('input_name', None)
		if name:
			results = results.filter(project_name__icontains = name)
			print('name: ',results)

		min_date = request.POST.get('input_min_date', None)
		if min_date:
			results = results.filter(publish_date__gte = min_date)
			print('min_date: ',results)

		max_date = request.POST.get('input_max_date', None)
		if max_date:
			results = results.filter(publish_date__lte = max_date)
			print('max_date: ',results)

		category = request.POST.getlist('input_category', None)
		if category:
			results = results.filter(category__in = category)
			print('cat:',category)
			print('category: ',request.POST['input_category'])

		return render(request,'project/index.html', {'form':  SearchForm(request.POST), 'project_list': results})

	return render(request,'project/index.html', {'form': SearchForm(),'project_list': results})
	

def createProject(request):
	if request.method == 'POST':
		form = CreateProjectForm(request.POST)
		if form.is_valid():
			p = form.save()
			
		return redirect('project_list')

	return render(request,'project/create_project.html',{'form': CreateProjectForm()})

