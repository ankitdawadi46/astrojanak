from django.db import models
from django.conf import settings

# Create your models here.
class service_book(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_type=models.CharField(max_length=50)

    def __str__(self):
         return self.user.username
