from django.shortcuts import get_object_or_404, render
from .models import Project, Category
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
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

		date = request.POST.get('input_request', None)
		if date:
			results = results.filter(publish_date=date)
			print('date: ',results)

		category = request.POST.get('input_category', None)
		if category:
			results = results.filter(category__in = category)
			print('category: ',results)

		return render(request,'project/index.html', {'form':  SearchForm(request.POST), 'project_list': results})

	return render(request,'project/index.html', {'form': SearchForm(),'project_list': results})
	

def createProject(request):
	if request.method == 'POST':
		form = CreateProjectForm(request.POST)
		if form.is_valid():
			p = form.save()
	return redirect('project_list')
			

