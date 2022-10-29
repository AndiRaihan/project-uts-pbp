from django.db import models
from auth.models import UserProfile
from forum.models import Forum

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    reply = models.OneToOneField(Forum)
    date = models.DateField(auto_now_add=True)