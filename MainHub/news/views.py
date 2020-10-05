from django.shortcuts import render
from .models import Slider


# Create your views here.
def index(request):
    data={
        'sliderData':Slider.objects.all
    }
    return render(request,"frontend/pages/home.html",data)
def about(request):
    return render(request,"frontend/pages/about.html")
def contact(request):
    return render(request,"frontend/pages/contact.html")
