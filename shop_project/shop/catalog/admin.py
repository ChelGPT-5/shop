from django.contrib import admin
from catalog.models import Category, Discount, Product, Seller, Promocode, Order, Cashback


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'articul', 'category', 'seller')
    search_fields = ('name', 'articul', 'seller__name', 'category__name', 'seller__country')
    list_select_related = ('category', 'seller')


admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Product, ProductAdmin)
admin.site.register(Promocode)
admin.site.register(Seller)
admin.site.register(Order)
admin.site.register(Cashback)
