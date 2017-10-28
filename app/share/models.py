from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
	user = models.OneToOneField (User, on_delete = models.CASCADE)
	def __str__(self):
		return self.user.username

class Project(models.Model):
	project_name = models.CharField(max_length = 20)
	pitch = models.TextField(max_length = 250)
	description = models.TextField()
	publish_date = models.DateTimeField('published date')
	accept_applicants = models.BooleanField()
	contact_email = models.EmailField()
	collaborators = models.ManyToManyField(CustomUser)
	def __str__(self):
		return self.project_name

class Categories(models.Model):
	category_name = models.CharField(max_length = 20)
	project_list = models.ManyToManyField(Project)
	def __str__(self):
		return self.category_name