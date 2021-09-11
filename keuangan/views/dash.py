from django.shortcuts import render, redirect
from ..models import CashFlow

def dash(request):
    html_template = 'keuangan/dash.html'

    getyear = int(request.GET.get('tahun', 2021))

    cashflow = CashFlow.objects.all().order_by('-tanggal').filter(tanggal__year = getyear)
    i = 1
    cashflowOutList = []
    cashflowInList = []
    while True:
        if i > 12:
            break
        monthCashFlow = cashflow.filter(tanggal__month = i)
        total = 0
        for monthCash in monthCashFlow:
            total += monthCash.harga_total
        cashflowOutList.append(total)
        cashflowInList.append(0)
        i += 1

    context = {
        'prevYear': getyear - 1,
        'thisYear': getyear,
        'nextYear': getyear + 1,
        'cashflowOutList': cashflowOutList,
        'cashflowInList': cashflowInList,

    }
    return render(request, html_template, context)