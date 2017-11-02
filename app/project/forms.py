from django import forms
from .models import Category, Project
# from user.models import CustomUser
class SearchForm(forms.Form):
    input_name = forms.CharField(label='Project Name', max_length=20, required = False)
    input_date = forms.DateField(label='Creation date', required = False)
    input_category = forms.ModelMultipleChoiceField(label='Category', queryset = Category.objects.all().order_by(
    	'category_name'))


class CreateProjectForm(forms.Form):
	name = forms.CharField(label = 'Project Name',max_length = 20)
	pitch = forms.CharField(label = 'Short Description', widget = forms.Textarea, max_length = 250)
	description = forms.CharField(label = 'Full Description', widget = forms.Textarea, max_length = 500)
	publish_date = forms.DateTimeField(label = 'Creation Date')
	accept_applicants = forms.BooleanField(label = 'Are you looking for collaborators?')
	contact_email = forms.EmailField(label = 'Contact Email', max_length = 70, required = False)
	# collaborators = models.ManyToManyField(CustomUser)
	category = forms.ModelMultipleChoiceField(label='Category', queryset = Category.objects.all().order_by(
    	'category_name'))

