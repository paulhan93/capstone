from re import M
from django.db import models

# Create your models here.
class Milestones(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()