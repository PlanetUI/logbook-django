from django.urls import path
from .views import detail, dashboard, index, edit, delete, save

urlpatterns = [
    path('', index),
    path('dashboard', dashboard),
    path('detail', detail),
    path('edit', edit),
    path('delete', delete),
    path('save', save),
]