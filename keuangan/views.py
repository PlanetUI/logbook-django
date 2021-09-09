from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    html_template = 'keuangan/index.html'
    context = {}
    return render(request, html_template, context)

def dashboard(request):
    total_01 = 0
    total_02 = 0
    total_03 = 0
    total_04 = 0
    total_05 = 0
    total_06 = 0
    total_07 = 0
    total_08 = 0
    total_09 = 0
    total_10 = 0
    total_11 = 0
    total_12 = 0

    html_template = 'keuangan/dashboard.html'
    cashflow = CashFlow.objects.all().order_by('-tanggal').filter(tanggal__year = request.GET.get('tahun', 2021))
    
    cashflow_01 = cashflow.filter(tanggal__month = 1)
    cashflow_02 = cashflow.filter(tanggal__month = 2)
    cashflow_03 = cashflow.filter(tanggal__month = 3)
    cashflow_04 = cashflow.filter(tanggal__month = 4)
    cashflow_05 = cashflow.filter(tanggal__month = 5)
    cashflow_06 = cashflow.filter(tanggal__month = 6)
    cashflow_07 = cashflow.filter(tanggal__month = 7)
    cashflow_08 = cashflow.filter(tanggal__month = 8)
    cashflow_09 = cashflow.filter(tanggal__month = 9)
    cashflow_10 = cashflow.filter(tanggal__month = 10)
    cashflow_11 = cashflow.filter(tanggal__month = 11)
    cashflow_12 = cashflow.filter(tanggal__month = 12)

    for cash in cashflow_01:
        total_01 += cash.harga_total
    for cash in cashflow_02:
        total_02 += cash.harga_total
    for cash in cashflow_03:
        total_03 += cash.harga_total
    for cash in cashflow_04:
        total_04 += cash.harga_total
    for cash in cashflow_05:
        total_05 += cash.harga_total
    for cash in cashflow_06:
        total_06 += cash.harga_total
    for cash in cashflow_07:
        total_07 += cash.harga_total
    for cash in cashflow_08:
        total_08 += cash.harga_total
    for cash in cashflow_09:
        total_09 += cash.harga_total
    for cash in cashflow_10:
        total_10 += cash.harga_total
    for cash in cashflow_11:
        total_11 += cash.harga_total
    for cash in cashflow_12:
        total_12 += cash.harga_total

    context = {
        'year': request.GET.get('tahun', '2021'),
        'cashflow': [
            {
                "no": 1,
                "bulan": "Januari",
                "total": total_01
            },
            {
                "no": 2,
                "bulan": "Februari",
                "total": total_02
            },
            {
                "no": 3,
                "bulan": "Maret",
                "total": total_03
            },
            {
                "no": 4,
                "bulan": "April",
                "total": total_04
            },
            {
                "no": 5,
                "bulan": "Mei",
                "total": total_05
            },
            {
                "no": 6,
                "bulan": "Juni",
                "total": total_06
            },
            {
                "no": 7,
                "bulan": "Juli",
                "total": total_07
            },
            {
                "no": 8,
                "bulan": "Agustus",
                "total": total_08
            },
            {
                "no": 9,
                "bulan": "September",
                "total": total_09
            },
            {
                "no": 10,
                "bulan": "Oktober",
                "total": total_10
            },
            {
                "no": 11,
                "bulan": "November",
                "total": total_11
            },
            {
                "no": 12,
                "bulan": "Desember",
                "total": total_12
            },
        ]
    }

    nama_bulan = []
    total_bulan = []
    for bln in context['cashflow']:
        nama_bulan.append(bln['bulan'])
        total_bulan.append(bln['total'])

    context['nama_bulan'] = nama_bulan
    context['total_bulan'] = total_bulan

    return render(request, html_template, context)

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

def edit(request):
    html_template = 'keuangan/edit.html'
    category = CashFlowCategory.objects.all()
    product = Product.objects.all()

    object_id = int(request.GET.get('id', 0))
    record = CashFlow.objects.get(pk=object_id)

    tanggal = str(request.GET.get('tanggal', 0))[0:10]

    context = {
        'category': category,
        'product': product,
        'tanggal': tanggal,
        'produk': record.produk
    }
    return render(request, html_template, context)

def save(request):
    o_id = int(request.GET.get('id', 0))
    kategory = request.GET.get('kategory', '')
    product = request.GET.get('product', '')
    qty = request.GET.get('qty', '')
    satuan = request.GET.get('satuan', '')
    tanggal = request.GET.get('tanggal', '')

    if (kategory != '') and (product != '') and (qty != '') and (satuan != '') and (tanggal != '') and (o_id != ''):
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

        object_id = int(request.GET.get('id', 0))

        record = CashFlow.objects.get(pk=object_id)
        record.kategory = obj_category
        record.produk = obj_product
        record.qty = int(qty)
        record.harga_satuan = float(satuan)
        record.tanggal = tanggal
        record.save()
    return redirect(f"/detail?tahun={request.GET.get('tahun','')}&bulan={request.GET.get('bulan','')}")

def delete(request):
    object_id = int(request.GET.get('id', 0))
    record = CashFlow.objects.filter(pk=object_id)
    record.delete()
    return redirect(f"/detail?tahun={request.GET.get('tahun','')}&bulan={request.GET.get('bulan','')}")

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