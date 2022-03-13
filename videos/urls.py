from django.conf.urls import url
from . import views
from django.urls import path
# SET THE NAMESPACE!
app_name = 'videos'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
  path('',views.video_list,name='video_list')
    
]