from django.contrib import admin
from .models import BasicProduct, BasicStore, StoreType, VipStore, VipProduct, VipCategory, VipCarruselIamge

# Basic page
class BasicProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class BasicStoreAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class StoreTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# vip page
class VipStoreAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class VipProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class VipCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class VipCarruselIamgeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(BasicProduct, BasicProductAdmin)
admin.site.register(BasicStore, BasicStoreAdmin)
admin.site.register(StoreType, StoreTypeAdmin)

admin.site.register(VipStore, VipStoreAdmin)
admin.site.register(VipProduct, VipProductAdmin)
admin.site.register(VipCategory, VipCategoryAdmin)
admin.site.register(VipCarruselIamge, VipCarruselIamgeAdmin)