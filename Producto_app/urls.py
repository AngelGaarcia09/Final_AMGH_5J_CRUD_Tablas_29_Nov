from django.urls import path 
from Producto_app import views

urlpatterns = [
    path("Producto",views.inicio_vista, name="Producto"),
    path("registrarProducto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<codigo>",views.seleccionarProducto,name="seleccionarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto"),
    path("borrarProducto/<codigo>",views.borrarProducto,name="borrarProducto")
]