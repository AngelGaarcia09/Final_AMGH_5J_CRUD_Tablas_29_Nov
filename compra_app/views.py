from django.shortcuts import render,redirect
from.models import Compra
# Create your views here.

def inicio_vista(request):
    loscompradores=Compra.objects.all()

    return render(request,"gestionarCompra.html",{"miscompradores":loscompradores})


def registrarCompra(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["txttelefono"]
    email=request.POST["txtemail"]
    cantidad=request.POST["txtcantidad"]
    direccion=request.POST["txtdireccion"]
    horario=request.POST["txthorario"]
    guardarcompra=Compra.objects.create(codigo=codigo,nombre=nombre,telefono=telefono,email=email,cantidad=cantidad,direccion=direccion,horario=horario)
    return redirect("Compra")

def seleccionarCompra(request,codigo):
    negocio=Compra.objects.get(codigo=codigo)
    return render(request,"editarCompra.html",{"miscompradores":negocio})

def editarCompra(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["txttelefono"]
    email=request.POST["txtemail"]
    cantidad=request.POST["txtcantidad"]
    direccion=request.POST["txtdireccion"]
    horario=request.POST["txthorario"]
    negocio=Compra.objects.get(codigo=codigo)
    negocio.nombre=nombre
    negocio.telefono=telefono
    negocio.email=email
    negocio.cantidad=cantidad
    negocio.direccion=direccion
    negocio.horario=horario
    negocio.save()
    return redirect("Compra")

def borrarCompra(request,codigo):
    materia=Compra.objects.get(codigo=codigo)
    materia.delete()
    return redirect("Compra")