from django.shortcuts import render
from categories.models import Category

# Create your views here.
def home(request):
    categories = Category.objects.all()
    return render(request, "core/index.html", {'categories':categories})

def services(request):
    return render(request, "core/services.html")

def contact(request):
    return render(request, "core/contact.html")

def about(request):
    return render(request, "core/about.html")