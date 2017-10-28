from django.contrib import admin
from .models import CustomUser, Project, Categories

admin.site.register(CustomUser)
admin.site.register(Project)
admin.site.register(Categories)