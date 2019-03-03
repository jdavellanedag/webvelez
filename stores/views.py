from django.shortcuts import render, get_object_or_404
from .models import BasicStore, BasicProduct, StoreType, VipStore

# Create your views here.
def basic_store(request, store_id):
    store = get_object_or_404(BasicStore, id=store_id)
    products = BasicProduct.objects.filter(store=store)
    return render(request, "stores/basic-store.html", {'store':store,
                                                        'products':products})

def vip_store(request, storevip_id):
    storevip = get_object_or_404(VipStore, id=storevip_id)
    return render(request, "stores/vip-store.html", {'storevip':storevip})