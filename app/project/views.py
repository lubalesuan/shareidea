from django.shortcuts import render,redirect
from django.urls import reverse
from django.utils import timezone, http

from .forms import SearchForm, CreateProjectForm
from .models import Project, Category

# view for index page
def index(request):

	#search dispatcher
	def search(query_set):
		results = Project.objects.all()
		query_set = dict(query_set)
		# searches is a dictionary of search functions
		searches = {
			# project name
			'pn': lambda x: results.filter(project_name__icontains = x),
			# earliest post date for project
			'psd': lambda x: results.filter(publish_date__gte = x),
			# latest post date for project
			'pgd': lambda x: results.filter(publish_date__lte = x),
			# project category
			'cat':lambda x: results.filter(category__in = eval(x)),
		}
		# if URL contains illgeal keys, filter them out
		key_set = set(query_set) & set(searches)
		# for each search parameter call corresponding search function
		for key in key_set:
			results = searches [key] (query_set[key].pop())
		return results

	# creating search form for the index page
	form = SearchForm(request.POST or None)
 	
	if request.method == 'POST' and form.is_valid():
		# data is a dictionary of search parameters
		data = {}
		for key in form.cleaned_data:
			# because 'cat' form field is a multiselect, put the choices in a list
			if form.cleaned_data['cat']:
				data['cat'] = request.POST.getlist('cat', None)
			# if a field was filled by user, put it in dictionary
			elif form.cleaned_data[key]:
				data[key] = form.cleaned_data[key]
		# pass dictionary as a query string to GET request
		q = http.urlencode(data)
		return redirect(reverse(index)+'?'+q)
	# render index page, pass search form to template, pass list of results from search to template
	return render(request,'project/index.html', {'form':form, 'project_list': search(request.GET)})

# renders project page, url ends with project id
def projectPage(request, pk = 0):
	pk = int(pk)
	# get project by id
	project = Project.objects.get(pk = pk)
	# render project page, pass project object to template
	return render(request, 'project/projectpage.html', {'project': project} )

# renders project creation page
def createProject(request):
	if request.method == 'POST':
		form = CreateProjectForm(request.POST)
		if form.is_valid():
			# save form to database
			p = form.save()	
			# redirect to index page
			return redirect('project_list')
	# if form is invalid or other requests, rerender project creation page
	return render(request,'project/create_project.html',{'form': CreateProjectForm()})

	