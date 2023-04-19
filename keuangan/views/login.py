from django.shortcuts import render

def login(request):
    html_template = 'keuangan/login.html'
    context = {}
    return render(request, html_template, context)