from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(ShippingAddress)
admin.site.register(BannerProduct)
admin.site.register(GaleriaFoto)
admin.site.register(Product_search)