from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=256)
    confirm_password = models.CharField(max_length=256)

    class Meta:
        unique_together = ('name', 'password')