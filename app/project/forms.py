from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Category, Project

from .models import Category

class SearchForm(forms.Form):
    input_name = forms.CharField(label='Project Name', max_length=20, required = False)
    input_date = forms.DateField(label='Creation date', required = False)
    input_category = forms.ModelMultipleChoiceField(label='Category', queryset = Category.objects.all().order_by(
    	'category_name'), required=False)


class CreateProjectForm(ModelForm):
 	class Meta:
 		model = Project
 		fields = ['project_name', 'pitch', 'description', 
 		'publish_date', 'accept_applicants', 'contact_email',
 		'category','collaborators']

 
class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = '__all__'
		widgets = {
			'color': TextInput(attrs={'type': 'color'}),
		}