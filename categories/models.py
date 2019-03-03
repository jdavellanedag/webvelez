from django.db import models
from stores.models import StoreType, BasicStore, VipStore

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="categories")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="categories")
    category = models.ForeignKey(Category, verbose_name="Categoría", on_delete=models.CASCADE, related_name="get_subcategories")
    store_type = models.ForeignKey(StoreType, verbose_name="Tipo", on_delete=models.CASCADE, related_name="get_type_store")
    basic_store = models.OneToOneField(BasicStore, verbose_name="Tienda básica", on_delete=models.CASCADE, related_name="get_basic_store", null=True, blank=True)
    vip_store = models.OneToOneField(VipStore, verbose_name="Tienda VIP", on_delete=models.CASCADE, related_name="get_vip_store", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "subcategoria"
        verbose_name_plural = "subcategorias"
        ordering = ['-created']
        
    def __str__(self):
        return self.title
