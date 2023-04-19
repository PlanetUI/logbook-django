from django.shortcuts import render

def home(request):
    html_template = 'keuangan/home.html'
    context = {}
    return render(request, html_template, context)