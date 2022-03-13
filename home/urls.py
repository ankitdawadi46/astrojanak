from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
# SET THE NAMESPACE!

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('',views.home,name='home'),
    path('registeruser',views.registeruser,name='registeruser'),
    path('login1',views.login,name='login'),
    path('login-page',views.login_page,name='login_page'),
    path('register-page',views.register_page,name='register_page'),
    path('login-user',views.loginuser,name='loginuser'),
    path('logout',views.logOut,name='logOut'),  
    path('reset-password/',
         auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
         name="reset_password"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_input.html"),
         name="password_reset_confirm"),
    path('reset-password-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
         name="password_reset_complete"),

]