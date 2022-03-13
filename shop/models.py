from django.db import models
from datetime import datetime,date
from django.conf import settings
from django.shortcuts import reverse,render,get_object_or_404
from .utils import get_unique_slug


class product_categories(models.Model):
    name = models.CharField(max_length=255, null=True)
    description=models.TextField(null=True)
    slug=models.SlugField(null=True,unique=True)
    image=models.ImageField(upload_to='',null=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("shop_detail",kwargs={'slug':self.slug})
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save(*args, **kwargs)
 

class products(models.Model):
    category = models.ForeignKey(product_categories, on_delete=models.CASCADE) 
    subcategory=models.CharField(max_length=255,unique=True)
    image = models.ImageField(upload_to='')
    
    slug=models.SlugField(null=True)
    description=models.TextField(null=True)
    added_on = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.subcategory
    def get_absolute_url(self):
        return reverse("rudra_detail",kwargs={'slug':self.slug})

class orders(models.Model):
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    order_product=models.ForeignKey(products, on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.order_product.subcategory

