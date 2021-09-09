from django.urls import path
# from .views import detail, dashboard, index, edit, delete, save

from .views.index import index
from .views.dashboard import dashboard
from .views.detail import detail
from .views.edit import edit, delete, save
from .views.category import category
from .views.product import product

urlpatterns = [
    path('', index),
    path('dashboard', dashboard),
    path('detail', detail),
    path('edit', edit),
    path('delete', delete),
    path('save', save),
    path('category', category),
    path('product', product),
]