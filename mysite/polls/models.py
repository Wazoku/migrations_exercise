from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Site for every client
class Site(models.Model):
    domain = models.CharField(max_length=10)
    description = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=255, null=True)

# Profile model including additional information
# about users
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dynamic_fields = models.JSONField(null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    bio = models.CharField(max_length=550, null=True)

# User profile forms for each site
class ProfileForm(models.Model):
    form_fields = models.JSONField()
    fields_data = models.JSONField(null=True)
    site=  models.ForeignKey(Site, on_delete=models.CASCADE)
    is_active = models.BooleanField(null=True)

# Store poll questions
class Poll(models.Model):
    title = models.CharField(max_length=100)

# Stores poll answers
class Answer(models.Model):
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name="answers",
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=250)
