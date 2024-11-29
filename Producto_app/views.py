from django.shortcuts import render,redirect
from.models import Producto
# Create your views here.

def inicio_vista(request):
    losproductos=Producto.objects.all()

    return render(request,"gestionarProducto.html",{"misproductos":losproductos})


def registrarProducto(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    precio=request.POST["txtprecio"]
    tipoprod=request.POST["txtprod"]
    descripcion=request.POST["txtdescripcion"]
    lote=request.POST["txtlote"]
    marca=request.POST["txtmarca"]
    guardarproducto=Producto.objects.create(codigo=codigo,nombre=nombre,precio=precio,tipoprod=tipoprod,descripcion=descripcion,lote=lote,marca=marca)
    return redirect("Producto")

def seleccionarProducto(request,codigo):
    negocio=Producto.objects.get(codigo=codigo)
    return render(request,"editarProducto.html",{"misproductos":negocio})

def editarProducto(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    precio=request.POST["txtprecio"]
    tipoprod=request.POST["txtprod"]
    descripcion=request.POST["txtdescripcion"]
    lote=request.POST["txtlote"]
    marca=request.POST["txtmarca"]
    negocio=Producto.objects.get(codigo=codigo)
    negocio.nombre=nombre
    negocio.precio=precio
    negocio.tipoprod=tipoprod
    negocio.descripcion=descripcion
    negocio.lote=lote
    negocio.marca=marca
    negocio.save()
    return redirect("Producto")

def borrarProducto(request,codigo):
    materia=Producto.objects.get(codigo=codigo)
    materia.delete()
    return redirect("Producto")