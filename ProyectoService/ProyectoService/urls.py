"""
URL configuration for ProyectoService project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from mantenimiento import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.buscarcliente, name='home'),
    path('buscarcliente/', views.buscarcliente),
    path('cliente/', views.cliente, name='cliente'),
    path('operario/', views.operario, name='operario'),
    path('mantenimiento/', views.mantenimiento, name='mantenimiento'),
    path('registrarcliente/', views.registrarCliente),
    path('registraroperario/', views.registrarOperario),
    path('registrarmantenimiento/', views.registrarMantenimiento),
    path('cliente/edicioncliente/<codigo>', views.edicionCliente),
    path('operario/edicionoperario/<codigo>', views.edicionOperario),
    path('mantenimiento/edicionmantenimiento/<codigo>', views.edicionMantenimiento),
    path('cliente/eliminarcliente/<codigo>', views.eliminarCliente),
    path('operario/eliminaroperario/<codigo>', views.eliminarOperario),
    path('mantenimiento/eliminarmantenimiento/<codigo>', views.eliminarMantenimiento),
    path('editarcliente/', views.editarCliente),
    path('editaroperario/', views.editarOperario),
    path('editarmantenimiento/', views.editarMantenimiento),
]
