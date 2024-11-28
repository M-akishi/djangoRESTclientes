
from django.urls import include, path
from .views import ClienteListCreateView

urlpatterns = [
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
]