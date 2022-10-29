from django.db import models
from authen.models import UserProfile, Content
from forum.models import Forum

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    comment = models.TextField()
    commented_on = models.ForeignKey(Content, on_delete=models.CASCADE)