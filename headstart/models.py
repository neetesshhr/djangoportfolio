from django.db import models

class GetImage(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField()
    #