from django.urls import path 
from compra_app import views

urlpatterns = [
    path("Compra",views.inicio_vista, name="Compra"),
    path("registrarCompra/",views.registrarCompra,name="registrarCompra"),
    path("seleccionarCompra/<codigo>",views.seleccionarCompra,name="seleccionarCompra"),
    path("editarCompra/",views.editarCompra,name="editarCompra"),
    path("borrarCompra/<codigo>",views.borrarCompra,name="borrarCompra")
]