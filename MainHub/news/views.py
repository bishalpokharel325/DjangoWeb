from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"frontend/pages/home.html")
def about(request):
    return render(request,"frontend/pages/about.html")
def contact(request):
    return render(request,"frontend/pages/contact.html")
