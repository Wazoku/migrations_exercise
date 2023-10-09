from django.contrib.auth.models import User
from django.db import models


# Site for every client
class Site(models.Model):
    domain = models.CharField(max_length=10)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)


# Profile model including additional information
# about users
class Profile(models.Model):
    bio = models.TextField(max_length=500, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dynamic_fields = models.JSONField(null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)


# User profile forms for each site
class ProfileForm(models.Model):
    form_fields = models.JSONField(blank=True, null=True, editable=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    is_active = models.BooleanField(null=True)
    fields_data = models.JSONField(blank=True, null=True)


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
