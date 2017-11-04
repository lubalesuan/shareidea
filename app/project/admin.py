from django.contrib import admin
from django.forms import ModelForm, TextInput
from django.contrib.admin import ModelAdmin
# from suit.widgets import HTML5Input

from .models import Project, Category


class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = '__all__'
		widgets = {
			'color': TextInput(attrs={'type': 'color'}),
		}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    fieldsets = (
        (None, {
            'fields': ('category_name', 'color')
            }),
        )


class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = '__all__'
		widgets = {
			'publish_date': TextInput(attrs={'type': 'date'}),
		}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    fieldsets = (
        (None, {
            'fields': ('project_name','pitch','publish_date',
            		'accept_applicants','contact_email','category','collaborators')
            }),
        )