from django.shortcuts import render, redirect

def category(request):
    html_template = 'keuangan/category.html'
    context = {}
    return render(request, html_template, context)