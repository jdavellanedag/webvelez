from django.db import models

# Create your models here.
class StoreType(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tipo")
    price = models.CharField(max_length=20, verbose_name="Precio")
    description = models.TextField(verbose_name="Descripcion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    class Meta:
        verbose_name = "tipo"
        verbose_name_plural = "tipos"
        ordering = ['-created']

    def __str__(self):
        return self.name

# Basic page

class BasicStore(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre tienda")
    content = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="stores")
    celphone = models.CharField(max_length=200, verbose_name="Celular", null=True, blank=True)
    phone = models.CharField(max_length=200, verbose_name="Telefono", null=True, blank=True)
    email = models.CharField(max_length=200, verbose_name="Correo electrónico", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "tienda basica"
        verbose_name_plural = "tiendas basicas"
        ordering = ['-created']

    def __str__(self):
        return self.title

class BasicProduct(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre producto")
    content = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="stores", null=True, blank=True)
    store = models.ForeignKey(BasicStore, verbose_name="Productos", on_delete=models.CASCADE, related_name="get_basic_products")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "producto basico"
        verbose_name_plural = "productos basicos"
        ordering = ['-created']

    def __str__(self):
        return self.title
    
# VIP page

class VipStore(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre tienda")
    content = models.TextField(verbose_name="Descripcion")
    celphone = models.CharField(max_length=200, verbose_name="Celular", null=True, blank=True)
    phone = models.CharField(max_length=200, verbose_name="Telefono", null=True, blank=True)
    email = models.CharField(max_length=200, verbose_name="Correo electrónico", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "tienda vip"
        verbose_name_plural = "tiendas vip"
        ordering = ['-created']

    def __str__(self):
        return self.title

class VipCarruselIamge(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    image = models.ImageField(verbose_name="Imagen", upload_to="stores", null=True, blank=True)
    store = models.ForeignKey(VipStore, verbose_name="Imagenes", on_delete=models.CASCADE, related_name="get_vip_images")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "catalogo vip imagen"
        verbose_name_plural = "catalogo vip imagenes"
        ordering = ['-created']

    def __str__(self):
        return self.title

class VipCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "categoria vip"
        verbose_name_plural = "categorias vip"
        ordering = ['-created']

    def __str__(self):
        return self.title

class VipProduct(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre producto")
    content = models.TextField(verbose_name="Descripcion")
    price = models.CharField(max_length=20, verbose_name="Precio")
    starts = models.PositiveSmallIntegerField(verbose_name="Estrellas")
    image = models.ImageField(verbose_name="Imagen", upload_to="stores", null=True, blank=True)
    store = models.ForeignKey(VipStore, verbose_name="Productos", on_delete=models.CASCADE, related_name="get_vip_products")
    category = models.ForeignKey(VipCategory, verbose_name="Categoría", on_delete=models.CASCADE, related_name="get_vip_category")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "producto vip"
        verbose_name_plural = "productos vip"
        ordering = ['-created']

    def __str__(self):
        return self.title