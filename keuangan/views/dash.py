from django.shortcuts import render, redirect

def dash(request):
    html_template = 'keuangan/dash.html'
    context = {}
    return render(request, html_template, context)