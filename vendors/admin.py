from django.contrib import admin
from vendors.models import Dealer, Product


@admin.action(description="Flush debt")
def flush_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'dealer_type', 'level', 'contractor', 'debt', 'country', 'city')
    list_filter = ('city', 'country')
    search_fields = ('name',)
    actions = [flush_debt]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'release_date')
    list_filter = ('release_date',)
    search_fields = ('name', 'model')
