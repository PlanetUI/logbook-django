from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime
import json
from ..models import CashFlow
from ..models import CashFlowCategory
from ..models import Product

def pengeluaran_form_get(request):
    html_template = 'keuangan/pengeluaran_form.html'

    getYear = int(request.GET.get('tahun', datetime.now().year))
    getMonth = int(request.GET.get('bulan', datetime.now().month))

    object_id = int(request.GET.get('id', 0))
    record = False
    if object_id != 0:
        record = CashFlow.objects.get(pk=object_id)
        record.tanggal = str(record.tanggal)[0:10]

    category = CashFlowCategory.objects.all()
    product = Product.objects.all()

    context = {
        'record': record,
        'category': category,
        'product': product,
        'thisYear': getYear,
        'thisMonth': getMonth,
        'thisDate': (
            f"{getYear}-{str(getMonth).zfill(2)}-{str(datetime.now().day).zfill(2)}"
        )
    }
    return render(request, html_template, context)

def pengeluaran_form_post(request):
    getYear = int(request.POST.get('tahun', datetime.now().year))
    getMonth = int(request.POST.get('bulan', datetime.now().month))
    getId = request.POST.get('id', 0)
    getTanggal = request.POST.get('tanggal', '0000-00-00')
    getKlasifikasi = request.POST.get('klasifikasi', '')
    getProduk = request.POST.get('produk', '')
    getQty = int(request.POST.get('qty', 0))
    getSatuan = float(request.POST.get('satuan', 0.0))

    try:
        obj_category = CashFlowCategory.objects.get(nama__exact=getKlasifikasi)
    except CashFlowCategory.DoesNotExist:
        obj_category = CashFlowCategory(nama=getKlasifikasi)
        obj_category.save()

    try:
        obj_product = Product.objects.get(nama__exact=getProduk)
    except Product.DoesNotExist:
        obj_product = Product(nama=getProduk)
        obj_product.save()

    if getId != '':
        # update
        record = CashFlow.objects.get(pk=int(getId))
        record.kategory = obj_category
        record.produk = obj_product
        record.qty = getQty
        record.harga_satuan = getSatuan
        record.tanggal = getTanggal
        record.save()
    else:
        # create
        obj_cashflow = CashFlow(
            kategory= obj_category,
            produk=obj_product,
            qty=getQty,
            harga_satuan=getSatuan,
            tanggal=getTanggal
        )
        obj_cashflow.save()

    return redirect(f"/pengeluaran?tahun={getYear}&bulan={getMonth}")

def pengeluaran_form_delete(request):
    body = request.body
    body_decode = body.decode('utf-8')
    body_json = json.loads(body_decode)
    record = CashFlow.objects.filter(pk=int(body_json['dataId']))
    record.delete()
    return JsonResponse({"status":"ok"})


def pengeluaran_form(request):
    if request.method == 'GET':
        return pengeluaran_form_get(request)
    elif request.method == 'POST':
        return pengeluaran_form_post(request)
    elif request.method == 'DELETE':
        return pengeluaran_form_delete(request)