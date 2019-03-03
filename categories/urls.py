from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name="categories"),
    path('category/<int:category_id>/', views.categories_list, name="categories_list"),
]
