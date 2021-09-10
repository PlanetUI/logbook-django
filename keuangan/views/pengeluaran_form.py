from django.shortcuts import render, redirect

def pengeluaran_form(request):
    html_template = 'keuangan/pengeluaran_form.html'
    context = {}
    return render(request, html_template, context)