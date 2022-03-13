from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('janmakundali/',views.janmakundali,name="janmakundali"),
    path('service-book/',views.servicebook,name="servicebook"),
    path('bhabishya-fal-kathan/',views.bhabisyaphalkathan,name="bhabisyaphalkathan"),
    path('bastu-paramarsa/',views.bastuparamarsa,name="bastuparamarsa"),
    path('graha-shanti/',views.grahashanti,name="grahashanti"),
    path('business-prediction/',views.businessprediction,name="businessprediction"),
   
    ] 
