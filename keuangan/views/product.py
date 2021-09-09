from django.shortcuts import render, redirect

def product(request):
    html_template = 'keuangan/product.html'
    context = {}
    return render(request, html_template, context)