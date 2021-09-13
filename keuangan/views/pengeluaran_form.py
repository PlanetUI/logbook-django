from django.shortcuts import render, redirect
from ..models import CashFlow

def pengeluaran_form(request):
    html_template = 'keuangan/pengeluaran_form.html'

    getYear = int(request.GET.get('tahun', 2021))
    getMonth = int(request.GET.get('bulan', 1))

    object_id = int(request.GET.get('id', 0))
    record = False
    if object_id != 0:
        record = CashFlow.objects.get(pk=object_id)
        record.tanggal = str(record.tanggal)[0:10]

    context = {
        'record': record,
        'thisYear': getYear,
        'thisMonth': getMonth,
    }
    return render(request, html_template, context)