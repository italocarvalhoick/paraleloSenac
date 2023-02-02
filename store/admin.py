from django.contrib import admin
from . models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image')
    
    list_display_links = ('id','name', 'price')

    #list_filter = ('nome', 'sobrenome')

    list_per_page = 10

    search_fields = ('name', 'price')



# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(ShippingAddress)
admin.site.register(BannerProduct)
admin.site.register(GaleriaFoto)
admin.site.register(Product_search)