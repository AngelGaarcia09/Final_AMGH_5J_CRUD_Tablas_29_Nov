from django.shortcuts import render,redirect
from.models import Sucursal
# Create your views here.

def inicio_vista(request):
    lossucursales=Sucursal.objects.all()

    return render(request,"gestionarSucursal.html",{"missucursales":lossucursales})


def registrarSucursal(request):
    codigo=request.POST["txtcodigo"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    horario=request.POST["txthorario"]
    nombre=request.POST["txtnombre"]
    email=request.POST["txtemail"]
    ciudad=request.POST["txtciudad"]
    guardarsucursal=Sucursal.objects.create(codigo=codigo,direccion=direccion,telefono=telefono,horario=horario,nombre=nombre,email=email,ciudad=ciudad)
    return redirect("Sucursal")

def seleccionarSucursal(request,codigo):
    negocio=Sucursal.objects.get(codigo=codigo)
    return render(request,"editarSucursal.html",{"missucursales":negocio})

def editarSucursal(request):
    codigo=request.POST["txtcodigo"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    horario=request.POST["txthorario"]
    nombre=request.POST["txtnombre"]
    email=request.POST["txtemail"]
    ciudad=request.POST["txtciudad"]
    negocio=Sucursal.objects.get(codigo=codigo)
    negocio.direccion=direccion
    negocio.telefono=telefono
    negocio.horario=horario
    negocio.nombre=nombre
    negocio.email=email
    negocio.ciudad=ciudad
    negocio.save()
    return redirect("Sucursal")

def borrarSucursal(request,codigo):
    materia=Sucursal.objects.get(codigo=codigo)
    materia.delete()
    return redirect("Sucursal")
