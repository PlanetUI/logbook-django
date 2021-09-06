from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

# Register your models here.
from .models import CashFlow, CashFlowCategory

class CashFlowAdmin(admin.ModelAdmin):
    list_display = ['tanggal', 'nama_item', 'qty', 'harga_satuan', 'harga_total']
    search_fields = ['tanggal', 'nama_item', 'qty', 'harga_satuan', 'harga_total']
    list_filter = ['tanggal', 'nama_item']

admin.site.register(CashFlow, CashFlowAdmin)
admin.site.register(CashFlowCategory)