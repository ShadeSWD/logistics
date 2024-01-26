from django.contrib import admin
from vendors.models import Dealer, Product


@admin.register(Dealer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'dealer_type', 'level', 'contractor', 'country', 'city')
    list_filter = ('city', 'country')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'release_date')
    list_filter = ('release_date',)
    search_fields = ('name', 'model')
