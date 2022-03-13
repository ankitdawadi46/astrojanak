from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import service_book
from smtplib import SMTPException
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def janmakundali(request):
    return render(request,"janma kundali.html")
def bhabisyaphalkathan(request):
    return render(request,"bhabishya_fal_kathan.html")
def bastuparamarsa(request):
    return render(request,"bastu paramarsa.html")
def grahashanti(request):
    return render(request,"Graha Shanti.html")
def businessprediction(request):
    return render(request,"Business Prediction.html")
def servicebook(request):
    if request.method=='POST':
        hidden_value=request.POST.get('hidden')
        if request.user.is_authenticated:
            print(request.user.email)
            subject="मेरो सेवाहरूको बुकिङको लागि हजुरलाई धन्यवाद छ |"
            message="नमस्ते "+str(request.user)+"!!! मेरो"+str(hidden_value)+" सेवाको बुकिङको लागि हजुरलाई धन्यवाद छ "
            from_email=settings.EMAIL_HOST_USER
            to_list=[request.user.email]
            try:
                send_mail(subject,message,from_email,to_list,fail_silently=False)
                serv=service_book(user=request.user,order_type=hidden_value)
                serv.save()
            except SMTPException as e:

                serv=service_book(user=request.user,order_type=hidden_value)
                serv.save()
         
    return redirect("/")