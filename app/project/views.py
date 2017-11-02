from django.shortcuts import get_object_or_404, render
from .models import Project, Category
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import SearchForm, CreateProjectForm

def index(request):
	name = ''
	date = ''
	category = ''
	project_list = None
	if request.method == 'POST':
		#create form instance, populate with data from 
		form = SearchForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['input_name'] or ''
			date = form.cleaned_data['input_date'] or ''
			category =  form.cleaned_data['input_category'] or ''
			project_list = Project.objects.filter(
				project_name__icontains = name,
				publish_date__icontains = date,
				category__in = category
			).distinct()
	else:
		form = SearchForm()	
		project_list = Project.objects.all()
	return render(request, 'project/index.html', 
		{'form':form, 'project_list':project_list})


def createProject(request):
	if request.method == 'POST':
		form = CreateProjectForm(request.POST)
		if form.is_valid():
			# name = form.cleaned_data['name']
			# pitch = form.cleaned_data['pitch']
			# description = form.cleaned_data['description']
			# publish_date = form.cleaned_data['publish_date']
			# accept_applicants = form.cleaned_data['accept_applicants']
			# contact_email = form.cleaned_data['contact_email']
			# category = form.cleaned_data['category']
			# p = Project(project_name = name,
			# 	pitch = pitch, description = description,
			# 	publish_date = publish_date, accept_applicants = accept_applicants,
			# 	contact_email = contact_email, category = category)
			# print("after valid")
			# p.save()
			p = Project(**form.cleaned_data)
			p.save()
			searchForm = SearchForm()
			project_list = Project.objects.all()
			# return HttpResponse(name)
			return render(request, 'project/index.html', 
				{'form':searchForm, 'project_list':project_list})
	else: 
		form = CreateProjectForm()
	return render(request, 'project/create_project.html', 
		{'form':form})
			
			


