from django.db import models
# from user.models import CustomUser
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
	category_name = models.CharField(max_length = 20)
	color = models.CharField(max_length = 7, blank=True, default='')

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.category_name

class Project(models.Model):
	project_name = models.CharField(max_length = 20)
	pitch = models.TextField(max_length = 250, blank=True)
	description = models.TextField(blank=True)
	publish_date = models.DateField('published date', default=datetime.date.today().strftime("%m/%d/%y"))
	accept_applicants = models.BooleanField(default=False)
	contact_email = models.EmailField()
	category = models.ForeignKey(Category, null=True)
	collaborators = models.ManyToManyField(User)
	
	def __str__(self):
		return self.project_name
 