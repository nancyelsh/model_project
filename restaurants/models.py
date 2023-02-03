from django.db import models

# Create your models here.
class Restaurant(models.Model):

    name = models.CharField(max_length=30)
    description = models.CharField(default="")
    opening_time = models.TimeField(auto_now=False, auto_now_add=False)
    closing_time = models.TimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
