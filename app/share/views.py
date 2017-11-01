from django.shortcuts import get_object_or_404, render
from .models import Project, CustomUser, Categories
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import SearchForm

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
				project_categories__category_name__icontains = category
			)
	else:
		form = SearchForm()	
		project_list = Project.objects.all()
	return render(request, 'share/index.html', 
		{'form':form, 'project_list':project_list})


