from django.db import models
from datetime import datetime,date

from django.conf import settings
from django.shortcuts import reverse,render,get_object_or_404

# Create your models here.
# Create your models here.
class blogs(models.Model):
    title=models.TextField()
    content=models.TextField()
    image=models.ImageField(upload_to='',blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slug=models.SlugField( null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("main_blog",kwargs={'slug':self.slug})