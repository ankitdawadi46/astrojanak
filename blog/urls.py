from django.urls import path
from . import views
from .views import bloglist, main_blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    path('',bloglist.as_view()),
    path('<slug:slug>',main_blog.as_view(), name='main_blog'),
   
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(urlpatterns)