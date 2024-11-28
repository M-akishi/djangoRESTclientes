from django.shortcuts import render

# Create your views here.
import csv
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer
from .filters import ClienteFilter
from .forms import ClienteForm
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, redirect, get_object_or_404
import pandas as pd


class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ClienteFilter
    
def listar_clientes(request):
    clientes = Cliente.objects.all()
    pg = Paginator(clientes, 25) 

    page_number = request.GET.get('page')
    page_obj = pg.get_page(page_number)

    return render(request, 'listClientes.html', {'page_obj': page_obj})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.delete()
    return redirect('listar_clientes')
    
    
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente) 
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'editClient.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('listar_clientes')
    else:
        form = ClienteForm()

    return render(request, 'createClient.html', {'form': form})

import pandas as pd
from django.shortcuts import render
from .models import Cliente

def estadistica(request):
    
    queryset = Cliente.objects.all().values()
    df = pd.DataFrame(queryset)
    
    describe_df = df.describe(include='all').to_html(classes="table table-striped")

    return render(request, 'estadistica.html', {'dataframe': describe_df})
