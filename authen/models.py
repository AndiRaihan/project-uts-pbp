from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    alias = models.CharField(max_length=255, default="Anonymous") # Beda sama username, bisa diganti gitu
    # TODO Mau ada field apa lagi?
 
class Content(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_captured = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_captured = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField()
    upvote_count = models.PositiveIntegerField(default=0)
    
    def get_creator_name(self):
        return self.creator.alias

class ContentUpvote(models.Model):
    content = models.OneToOneField(Content, on_delete=models.CASCADE)
    upvoter = models.ManyToManyField(UserProfile)
    
    def get_upvote(self):
        return self.upvoter.distinct().count()
    