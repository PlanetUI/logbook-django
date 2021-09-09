from django.shortcuts import render, redirect

def index(request):
    html_template = 'keuangan/index.html'
    context = {}
    return render(request, html_template, context)