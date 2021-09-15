from django.urls import path
# from .views import detail, dashboard, index, edit, delete, save

from .views.detail import detail
from .views.edit import edit, delete, save
from .views.category import category
from .views.product import product
from .views.home import home
from .views.dash import dash
from .views.pengeluaran import pengeluaran
from .views.pengeluaran_form import pengeluaran_form
from .views.pemasukan import pemasukan

urlpatterns = [
    path('', home),
    path('dash', dash),
    path('pengeluaran', pengeluaran),
    path('pengeluaran_form', pengeluaran_form),
    path('pemasukan', pemasukan),
    path('detail', detail),
    path('edit', edit),
    path('delete', delete),
    path('save', save),
    path('category', category),
    path('product', product),
]