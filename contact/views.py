
from .models import contactform
from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from smtplib import SMTPException
# Create your views here.
def contactform1(request):
    if request.method=='POST':
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        telephone=request.POST.get('telephone')
        msg=request.POST.get('msg')
        a=0
        for i in email:
            if i=='@':
                a=1

        if a==1 or not(full_name or telephone or msg)=="":    
        #sending mail
            subj="Thank you for contacting us!!"
            message="Hello "+full_name+"!. Thank you for contacting us. We will be in touch soon."
            from_email=settings.EMAIL_HOST_USER
            to_list=[email]
            try:
                send_mail(subj,message,from_email,to_list,fail_silently=False)
                cont=contactform(full_name=full_name,email=email,phone=telephone,desc=msg,is_replied=True)
                cont.save()
            except SMTPException as e:
                print("Is hero")
                cont=contactform(full_name=full_name,email=email,phone=telephone,desc=msg,is_replied=False)
                cont.save()
            return redirect("/")
        else:
            return redirect("/")

    else:
        return redirect("/")
