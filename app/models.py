from django.db import models

# Create your models here.
class Plane(models.Model):
    firstname = models.CharField(max_length=25,null=False)
