from django.db import models
from random import randint


# Create your models here.
class Tweet(models.Model):
    content = models.CharField(blank=True, null=True, max_length=280)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    class Meta:
        ordering = ['-id']

        def __str__(self):
            return f"Tweet id {self.pk} and tweet: {self.content}"

    def rand_likes(self):
        return str(randint(0, 100))

    def serialize(self):
        return {
            "pk": self.pk,
            "content": self.content,
            "likes": randint(0, 100)
        }
