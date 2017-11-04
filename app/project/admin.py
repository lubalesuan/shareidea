from django.contrib import admin
from .models import Project, Category
from .forms import CategoryForm


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    model=Category
    fieldsets = (
        (None, {
            'fields': ('category_name', 'color')
            }),
        )

admin.site.register([Project, Category])

