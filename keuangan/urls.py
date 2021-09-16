from django.urls import path
from .views.category import category
from .views.product import product
from .views.home import home
from .views.dash import dash
from .views.pengeluaran import pengeluaran
from .views.pengeluaran_form import pengeluaran_form
from .views.pemasukan import pemasukan
from .views.login import login

urlpatterns = [
    path('', home),
    path('login', login),
    path('dash', dash),
    path('pengeluaran', pengeluaran),
    path('pengeluaran_form', pengeluaran_form),
    path('pemasukan', pemasukan),
    path('category', category),
    path('product', product),
]