from django.db import models

class Art(models.Model):

    title = models.CharField(max_length=128, null=False, default='')
    art = models.TextField(null=False, default='')
    created = models.DateTimeField(auto_now_add=True)
    lat = models.CharField(max_length=64, null=True)
    lon = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.title