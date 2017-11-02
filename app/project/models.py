from django.db import models
# from user.models import CustomUser

class Category(models.Model):
	category_name = models.CharField(max_length = 20)
	def __str__(self):
		return self.category_name

class Project(models.Model):
	project_name = models.CharField(max_length = 20)
	pitch = models.TextField(max_length = 250)
	description = models.TextField()
	publish_date = models.DateTimeField('published date')
	accept_applicants = models.BooleanField()
	contact_email = models.EmailField()
	category = models.ManyToManyField(Category)
	def __str__(self):
		return self.project_name
