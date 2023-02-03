from django.db import models

# Create your models here.
class Restaurant(models.Model):

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250, default="")
    opening_time = models.TimeField(auto_now=False, auto_now_add=False)
    closing_time = models.TimeField(auto_now=False, auto_now_add=False)
    open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.opening_time} {self.closing_time} {self.created_at}"
