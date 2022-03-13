from django.db import models
from nepali_date import NepaliDate
# Create your models here.
class horoscope1(models.Model):
    year=models.IntegerField(null=True)
    month=models.CharField(null=True,max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    Mesh=models.TextField(null=True)
    Brish=models.TextField(null=True)
    Mithun=models.TextField(null=True)
    Karkat=models.TextField(null=True)
    Singha=models.TextField(null=True)
    Kanya=models.TextField(null=True)
    Tula=models.TextField(null=True)
    Brischik=models.TextField(null=True)
    Dhan=models.TextField(null=True)
    Makar=models.TextField(null=True)
    Kumbha=models.TextField(null=True)
    Min=models.TextField(null=True)

    def __str__(self):
        return (str(self.year) + "/" +self.month)