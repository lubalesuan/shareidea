from django import forms

class SearchForm(forms.Form):
    input_name = forms.CharField(label='Project name', max_length=100)
    input_date = forms.DateField(label='Creation date')
    input_category = forms.CharField(label='Category', max_length=100)