from django.shortcuts import render, redirect

from ..models import *

def save_cashflow(request):
    kategory = request.GET.get('kategory', '')
    product = request.GET.get('product', '')
    qty = request.GET.get('qty', '')
    satuan = request.GET.get('satuan', '')
    tanggal = request.GET.get('tanggal', '')

    if (kategory != '') and (product != '') and (qty != '') and (satuan != '') and (tanggal != ''):
        try:
            obj_category = CashFlowCategory.objects.get(nama__exact=kategory)
        except:
            obj_category = CashFlowCategory(nama=kategory)
            obj_category.save()

        try:
            obj_product = Product.objects.get(nama__exact=product)
        except:
            obj_product = Product(nama=product)
            obj_product.save()


        obj_cashflow = CashFlow(
            kategory= obj_category,
            produk=obj_product,
            qty=int(qty),
            harga_satuan=float(satuan),
            tanggal=tanggal
        )
        obj_cashflow.save()

def detail(request):
    save_cashflow(request)
    html_template = 'keuangan/detail.html'

    current_month = int(request.GET.get('bulan', 1))
    current_year = int(request.GET.get('tahun', 2021))

    if current_month == 12:
        next_year = current_year + 1
        prev_year = current_year
        next_month = 1
        prev_month = current_month - 1
    elif current_month == 1:
        next_year = current_year
        prev_year = current_year - 1
        next_month = current_month + 1
        prev_month = 12
    else:
        next_year = current_year
        prev_year = current_year
        next_month = current_month + 1
        prev_month = current_month - 1
    
    cashflow = CashFlow.objects.all().order_by('-pk').filter(tanggal__year = request.GET.get('tahun', 2021), tanggal__month = current_month)

    total = 0
    list_kategori = []
    total_kategori = []
    for cash in cashflow:
        total += cash.harga_total
        if str(cash.kategory) not in list_kategori:
            list_kategori.append(str(cash.kategory))
            total_kategori.append(0)

    for key, value in enumerate(list_kategori):
        for cash in cashflow:
            if value == str(cash.kategory):
                total_kategori[key] += cash.harga_total

    bulan = {
        "1": "January",
        "2": "February",
        "3": "Maret",
        "4": "April",
        "5": "Mei",
        "6": "Juni",
        "7": "Juli",
        "8": "Agustus",
        "9": "September",
        "10": "Oktober",
        "11": "November",
        "12": "Desember",
    }

    category = CashFlowCategory.objects.all()
    product = Product.objects.all()

    context = {
        'year': str(current_year),
        'month': bulan[request.GET.get('bulan', '1')],
        'current_month': current_month,
        'cashflow': cashflow,
        'total': total,
        'list_kategori': list_kategori,
        'total_kategori': total_kategori,
        'next_year': str(next_year),
        'next_month': str(next_month),
        'prev_year': str(prev_year),
        'prev_month': str(prev_month),
        'category': category,
        'product': product,
        'digit2': [10, 11, 12]
    }
    return render(request, html_template, context)