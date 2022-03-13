from django.db import models
from phone_field import PhoneField

# Create your models here.
class contactform(models.Model):
    full_name = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    desc = models.TextField()
    is_replied=models.BooleanField(null=False)
     
    def get_absolute_url(self):
        return reverse("resolve",kwargs={"id":self.id})