from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    alias = models.CharField(max_length=255) # Beda sama username, bisa diganti gitu
    # TODO Mau ada field apa lagi?
 
class Content(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_captured = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_captured = models.DateTimeField(blank=True)
    photo = models.ImageField()
    upvoter = models.ManyToManyField(UserProfile)