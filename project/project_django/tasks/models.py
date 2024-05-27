from django.db import models # type: ignore

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()