from django.shortcuts import render

def pemasukan(request):
    html_template = 'keuangan/pemasukan.html'
    context = {}
    return render(request, html_template, context)