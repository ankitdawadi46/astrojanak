from django.shortcuts import render
from .models import horoscope1

# Create your views here.
def horoscope(request):
    horoscope2=horoscope1.objects.latest('date_added')
    print(horoscope2)
    return render(request,"horoscope.html",{"horoscope":horoscope2})