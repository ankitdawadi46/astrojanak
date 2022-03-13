from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from .models import products, product_categories,orders
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class shop_home(ListView):
    model=product_categories
    template_name='shop.html'

def rudracard(request):
    return render(request,"rudracard.html")

class shop_detail(DetailView):
    model=product_categories
    template_name='rudracard.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(shop_detail, self).get_context_data(*args, **kwargs)
        print(self.kwargs)
        context['product_list'] = products.objects.filter(category_id=product_categories.objects.get(slug=self.kwargs.get('slug')).pk)
        return context


class rudra_detail(DetailView):
    model=products
    template_name='rudrakshya.html'

def book_management(request):
    if request.method=='POST':
        hidden_value=request.POST.get('hidden')
        queryset=products.objects.get(subcategory=hidden_value).pk
        subject="मेरो सामानहरूको बुकिङको लागि हजुरलाई धन्यवाद छ |"
        message="नमस्ते "+str(request.user)+"!!! मेरो "+str(hidden_value)+" सामानको बुकिङको लागि हजुरलाई धन्यवाद छ |"
        from_email=settings.EMAIL_HOST_USER
        to_list=[request.user.email]
        try:
            send_mail(subject,message,from_email,to_list,fail_silently=False)
            order=orders(user_id=request.user.id,order_product_id=queryset,ordered=True)
            order.save()
        except SMTPException as e:
            order=orders(user_id=request.user.id,order_product_id=queryset,ordered=True)
            order.save()
        
    return redirect("/")