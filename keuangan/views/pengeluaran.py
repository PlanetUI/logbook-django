from django.shortcuts import render, redirect
from datetime import datetime
from ..models import CashFlow


def monthString(number=datetime.now().month):
    data = {
        1: 'Januari',
        2: 'February',
        3: 'Maret',
        4: 'April',
        5: 'Mei',
        6: 'Juni',
        7: 'Juli',
        8: 'Agustus',
        9: 'September',
        10: 'Oktober',
        11: 'November',
        12: 'Desember',
    }
    return data[number]

def getCashFlow(tahun=datetime.now().year, bulan=datetime.now().month):
    cashFlow = CashFlow.objects.all().order_by('-pk').filter(tanggal__year = tahun, tanggal__month = bulan)

    total = 0
    list_kategori = []
    total_kategori = []
    list_product = []
    total_product = []
    for cash in cashFlow:
        total += cash.harga_total
        if str(cash.kategory) not in list_kategori:
            list_kategori.append(str(cash.kategory))
            total_kategori.append(0)
        if str(cash.produk) not in list_product:
            list_product.append(str(cash.produk))
            total_product.append(0)

    for key, value in enumerate(list_kategori):
        for cash in cashFlow:
            if value == str(cash.kategory):
                total_kategori[key] += cash.harga_total
                
    for key, value in enumerate(list_product):
        for cash in cashFlow:
            if value == str(cash.produk):
                total_product[key] += cash.harga_total
    return {
        'total': total,
        'cashFlow': cashFlow,
        'list_kategori': list_kategori,
        'total_kategori': total_kategori,
        'list_product': list_product,
        'total_product': total_product,

    }

def pengeluaran(request):
    html_template = 'keuangan/pengeluaran.html'

    getYear = int(request.GET.get('tahun', datetime.now().year))
    getMonth = int(request.GET.get('bulan', datetime.now().month))
    getView = str(request.GET.get('view', 'tree'))

    if getMonth == 1:
        prevYear = getYear - 1
        prevMonth = 12
        nextYear = getYear
        nextMonth = getMonth + 1
    elif getMonth == 12:
        prevYear = getYear
        prevMonth = getMonth - 1
        nextYear = getYear + 1
        nextMonth = 1
    else:
        prevYear = getYear
        prevMonth = getMonth - 1
        nextYear = getYear
        nextMonth = getMonth + 1

    context = {
        'thisYear': getYear,
        'thisMonth': getMonth,
        'thisMonthString': monthString(getMonth),
        'prevYear': prevYear,
        'prevMonth': prevMonth,
        'nextYear': nextYear,
        'nextMonth': nextMonth,
        'getView': getView,
        'data': getCashFlow(getYear, getMonth),
        'thisDate': f"{getYear}-{str(getMonth).zfill(2)}-{str(datetime.now().day).zfill(2)}"
    }
    return render(request, html_template, context)