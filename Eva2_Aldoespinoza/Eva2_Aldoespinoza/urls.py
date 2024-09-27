"""
URL configuration for Eva2_Aldoespinoza project.

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
# Eva2_Aldoespinoza/urls.py
from django.contrib import admin
from django.urls import path
from modelFormApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyectos/', views.listadoProyectos, name='listadoProyectos'),
    path('agregarProyecto/', views.agregarProyecto, name='agregarProyecto'),
    path('eliminarProyecto<int:id>/', views.eliminarProyecto, name='eliminarProyecto'),
    path('actualizarProyecto/<int:id>/', views.actualizarProyecto, name='actualizarProyecto'),
]