from django.db import models
from django.contrib.auth.models import User
from forum.models import forum

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    liked = models.ForeignKey(forum, on_delete=models.CASCADE)