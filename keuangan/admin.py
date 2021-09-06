from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

# Register your models here.
from .models import CashFlow, CashFlowCategory

class CashFlowAdmin(admin.ModelAdmin):
    list_display = ['tanggal', 'kategory', 'nama_item', 'qty', 'harga_satuan', 'harga_total']
    search_fields = ['tanggal', 'kategory', 'nama_item', 'qty', 'harga_satuan', 'harga_total']
    list_filter = ['tanggal', 'kategory', 'nama_item']

admin.site.register(CashFlow, CashFlowAdmin)
admin.site.register(CashFlowCategory)