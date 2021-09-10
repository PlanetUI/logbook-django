from django.shortcuts import render, redirect

def home(request):
    html_template = 'keuangan/home.html'
    context = {}
    return render(request, html_template, context)