from django.urls import path
from . import views
from .views import rudra_detail,shop_detail
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[

    path('',views.shop_home.as_view()),
    
    path('<slug:slug>',shop_detail.as_view(),name='shop_detail'),
    
    path('products/<slug:slug>',rudra_detail.as_view(), name='rudra_detail'),

    path('/book_management',views.book_management,name='book_management'),
   
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)