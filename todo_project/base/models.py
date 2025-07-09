from django.db import models

# Create your models here.
class todo(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(max_length=300)


class todo_type(models.Model):
    name = models.CharField(max_length=100)