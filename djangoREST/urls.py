"""
URL configuration for djangoREST project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from api import views

urlpatterns = [
    path('', RedirectView.as_view(url='clientes/')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),    
    path('clientes/new/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),    
    path('clientes/eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'), 
    path('clientes/editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('estadistica/',views.estadistica, name='estadistica')    
]
