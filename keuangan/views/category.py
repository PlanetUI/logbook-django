from django.shortcuts import render, redirect
from ..models import CashFlowCategory

def category(request):
    html_template = 'keuangan/category.html'

    cashFlowCategory = CashFlowCategory.objects.all().order_by('-pk')

    context = {'cashFlowCategory': cashFlowCategory}
    return render(request, html_template, context)