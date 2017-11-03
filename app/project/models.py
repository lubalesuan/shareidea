from django.db import models
# from user.models import CustomUser
from django.contrib.auth.models import User

class Category(models.Model):
	category_name = models.CharField(max_length = 20)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.category_name

class Project(models.Model):
	project_name = models.CharField(max_length = 20)
	pitch = models.TextField(max_length = 250)
	description = models.TextField()
	publish_date = models.DateTimeField('published date')
	accept_applicants = models.BooleanField()
	contact_email = models.EmailField()
	category = models.ForeignKey(Category)
	collaborators = models.ManyToManyField(User)
	
	def __str__(self):
		return self.project_name
