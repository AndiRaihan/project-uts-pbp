from django.db import models


# Create your models here.
class Corruptor(models.Model):
    name = models.CharField(max_length=100)
    arrested_date = models.DateField()
    corruption_type = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateField(auto_now=True)