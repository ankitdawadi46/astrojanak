"""
Definition of urls for JanakBhatta.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include("home.urls")),
    path('',include("django.contrib.auth.urls")),
    path('',include("contact.urls")),
    path('horoscope',include("horoscope.urls")),
    path('blog/',include("blog.urls")),
    path('shop',include("shop.urls")),
    path('videos/',include("videos.urls")),
    path('',include("services.urls")),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
