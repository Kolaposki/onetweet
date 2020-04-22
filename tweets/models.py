from django.db import models


# Create your models here.
class Tweet(models.Model):
    text = models.CharField(blank=True, null=True, max_length=256)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
