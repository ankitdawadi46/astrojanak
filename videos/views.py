from django.shortcuts import render
from .models import videos

# Create your views here.
def video_list(request):
    video=videos.objects.order_by('-updated_on')
    return render(request,"videos.html",{'videos':video})