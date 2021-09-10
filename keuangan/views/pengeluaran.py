from django.shortcuts import render, redirect

def pengeluaran(request):
    html_template = 'keuangan/pengeluaran.html'
    context = {}
    return render(request, html_template, context)