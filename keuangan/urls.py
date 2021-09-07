from django.urls import path
from .views import dashboard, index

urlpatterns = [
    path('', index),
    path('dashboard', dashboard),
]