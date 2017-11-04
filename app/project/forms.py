from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Category, Project

from .models import Category

class SearchForm(forms.Form):
    input_name = forms.CharField(label='Project', max_length=20, required = False)
    input_min_date = forms.DateField(label='Earliest', required = False,widget=TextInput(attrs={'type': 'date'}) )
    input_max_date = forms.DateField(label='Latest', required = False,widget=TextInput(attrs={'type': 'date'}) )
    input_category = forms.ModelMultipleChoiceField(label='Category', queryset = Category.objects.all().order_by(
    	'category_name'), required=False)

class CreateProjectForm(ModelForm):
 	class Meta:
 		model = Project
 		fields = ['project_name', 'pitch', 'description', 
 		'publish_date', 'accept_applicants', 'contact_email',
 		'category','collaborators']

 		widgets = {
			'publish_date': TextInput(attrs={'type': 'date'}),
		}
 
