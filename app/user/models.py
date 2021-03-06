from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class CustomUser(models.Model):
# 	user = models.OneToOneField (User, on_delete = models.CASCADE)
# 	projects_wanted = models.BooleanField()
# 	email_confirmed = models.BooleanField(default=False)

# 	def __str__(self):
# 		return self.user.username

class Profile(models.Model):
	user = models.OneToOneField (User, on_delete = models.CASCADE)
	projects_wanted = models.BooleanField(default=False)
	email_confirmed = models.BooleanField(default=False)
	
	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()