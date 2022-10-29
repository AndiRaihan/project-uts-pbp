from django.db import models
from authen.models import UserProfile, Content

# Create your models here.

class Forum(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE) # Perlu kah?
    title = models.CharField(max_length = 255, unique=True)
    description = models.TextField()
    contents = models.ManyToManyField(Content)
    date_created = models.DateTimeField(auto_now_add=True)
    
class Members(models.Model):
    forum = models.OneToOneField(Forum, on_delete=models.CASCADE)
    subscriptor = models.ManyToManyField(UserProfile) # Mau make ginian?