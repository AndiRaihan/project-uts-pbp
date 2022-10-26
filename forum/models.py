from django.db import models
from auth.models import UserProfile

# Create your models here.

class Forum(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    is_captured = models.BooleanField()
    date_created = models.DateTimeField()
    date_captured = models.DateTimeField()
    photo = models.ImageField()
    upvote_count = models.PositiveIntegerField()