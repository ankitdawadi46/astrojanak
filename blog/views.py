from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import blogs

# Create your views here.
class bloglist(ListView):
    model= blogs
    queryset = blogs.objects.order_by('-updated_on')

class main_blog(DetailView):
    model=blogs
    template_name='insideblog.html'