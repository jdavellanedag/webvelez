from django.urls import path
from . import views

urlpatterns = [
    path('basic/<int:store_id>/', views.basic_store, name="basic_store"),
    path('vip/<int:storevip_id>/', views.vip_store, name="vip_store"),
]
