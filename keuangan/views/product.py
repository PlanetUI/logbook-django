from django.shortcuts import render
from ..models import Product


def product(request):
    html_template = 'keuangan/product.html'

    product = Product.objects.all().order_by('-pk')

    context = {'product': product}
    return render(request, html_template, context)
