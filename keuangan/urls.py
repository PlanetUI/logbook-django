from django.urls import path
from .views import detail, dashboard, index

urlpatterns = [
    path('', index),
    path('dashboard', dashboard),
    path('detail', detail),
]