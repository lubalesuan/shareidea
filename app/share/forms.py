from django import forms

class SearchForm(forms.Form):
    input_name = forms.CharField(label='Project name', max_length=100, required = False)
    input_date = forms.DateField(label='Creation date', required = False)
    input_category = forms.CharField(label='Category', max_length=100, required = False)