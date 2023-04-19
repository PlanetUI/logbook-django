from django.contrib import admin

# Register your models here.
from .models import Product, CashFlow, CashFlowCategory

class CashFlowAdmin(admin.ModelAdmin):
    list_display = [
        'tanggal', 'kategory', 'produk', 'qty', 'harga_satuan', 'harga_total'
    ]
    search_fields = ['produk']
    list_filter = ['tanggal', 'kategory', 'produk']

admin.site.register(CashFlow, CashFlowAdmin)
admin.site.register(CashFlowCategory)
admin.site.register(Product)