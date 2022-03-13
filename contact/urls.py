from django.conf.urls import url
from . import views
from django.urls import path
# SET THE NAMESPACE!

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('/contactform1', views.contactform1, name='contactform1'),
]