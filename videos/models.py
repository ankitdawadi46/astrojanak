from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class videos(models.Model):
    title=models.TextField()
    description=models.TextField()
    video=EmbedVideoField(default="https://www.youtube.com/watch?v=USBNA9XvAjw")
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title