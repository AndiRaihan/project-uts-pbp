from django.db import models
from authen.models import UserProfile

# Create your models here.

class Admin(UserProfile):
    UserProfile.is_admin = True
    active_since = models.DateField(auto_now_add=True)
