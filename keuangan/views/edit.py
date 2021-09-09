from django.shortcuts import render, redirect

from ..models import *

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
