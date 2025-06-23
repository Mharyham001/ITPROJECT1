from django.contrib import admin
from .models import product, order
from django.contrib.auth.models import Group

admin.site.site_header = 'AuxanoInventory Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ('category',) 


# Register your models here.
admin.site.register(product, ProductAdmin)
admin.site.register(order)