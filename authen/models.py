from django.db import models
from django.contrib.auth.models import User
#from forum.models import Forum

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #liked = models.ForeignKey(Forum, on_delete=models.CASCADE)
    image = models.ImageField()