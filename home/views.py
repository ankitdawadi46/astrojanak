
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from .models import webusers
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout



# Create your views here.

def logOut(request):
    auth.logout(request)
    print("Hello")
    return redirect("/")
#home view rendering
def home(request):
    return render(request,"index (2).html")

def login(request):
    return render(request,"registration/login.html")

#registering new users
def registeruser(request):
    if request.method=="POST":
        first_name=request.POST["fname"]
        last_name=request.POST["lname"]
        email=request.POST["email"]
        phone=request.POST["phn"]
        location=request.POST["location"]
        password=request.POST["pwd"]
        repassword=request.POST["repwd"]
        username=request.POST["username"]
        if (User.objects.filter(username=username).count()>=1):
            messages.warning(request, 'The username already exists')
            return redirect("/register-page")
        elif(User.objects.filter(email=email).count()>=1):
            messages.warning(request,'The email id already exists')
            return redirect("/register-page")
        else:
            if(password==repassword):
                user=User.objects.create(first_name=first_name, last_name=last_name, email=email,username=username)
                user.set_password(password)
                user.save()
                webuser=webusers(user_details=user,location=location, contactno=phone)
                webuser.save()
            else:
                messages.warning(request, 'Your password fields does not match.')
                return redirect("/register-page")
        return redirect("/")

#login for users 
@never_cache
def loginuser(request):
    
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                user1=user
                if user1 is not None:
                    auth.login(request,user1)
                    request.session['is_logged']=True
                    return redirect("/")
                else:
                    messages.warning(request,"Sorry!!!! You do not have the required credentials to login.")
            else:
                messages.warning(request,"Sorry!!!! You do not have the required credentials to login.")
            return redirect("/")
        except:
            messages.warning(request,"Sorry!!!! You do not have the required credentials to login.")
    else:
        
        return redirect("/")
    return redirect("/")

# rendering the home page with login page
def login_page(request):
    return render(request,"index (2).html")

#rendering the homepage with the registration page
def register_page(request):
    return render(request,"register1.html")

def horoscope(request):
    return render(request,"horoscope.html")

