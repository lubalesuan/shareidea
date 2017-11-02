from django import forms
from .models import Category
class SearchForm(forms.Form):
    input_name = forms.CharField(label='Project name', max_length=100, required = False)
    input_date = forms.DateField(label='Creation date', required = False)
    input_category = forms.ModelMultipleChoiceField(label='Category', queryset = Category.objects.all().order_by(
    	'category_name'))
