from django.shortcuts import render, get_object_or_404
from .models import Category, Subcategory

# Create your views here.
def categories(request):
    categories = Category.objects.all()
    return render(request, "categories/categories.html", {'categories':categories})

def categories_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "categories/categories-list.html", {'category':category})
