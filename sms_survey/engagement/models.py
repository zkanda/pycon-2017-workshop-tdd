from django.db import models

# Create your models here.

class Messages(models.Model):
    mobile_number = models.CharField(max_length=20)
    message = models.TextField()