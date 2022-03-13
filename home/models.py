from django.db import models
from phone_field import PhoneField
from django.conf import settings

class webusers(models.Model):
    user_details = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField("Address", max_length=50, blank=True)
    contactno=PhoneField(null=True)
    
    def __str__(self):
        return self.user_details.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

