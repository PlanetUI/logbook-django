from django.shortcuts import render, redirect

def dash(request):
    html_template = 'keuangan/dash.html'

    getyear = int(request.GET.get('tahun', 2021))

    context = {
        'prevYear': getyear - 1,
        'thisYear': getyear,
        'nextYear': getyear + 1

    }
    return render(request, html_template, context)