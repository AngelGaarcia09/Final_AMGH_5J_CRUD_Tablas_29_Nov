from django.shortcuts import render,redirect
from.models import Cliente
# Create your views here.

def inicio_vista(request):
    losclientes=Cliente.objects.all()

    return render(request,"gestionarCliente.html",{"misclientes":losclientes})


def registrarCliente(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["txttelefono"]
    direccion=request.POST["txtdireccion"]
    apellidom=request.POST["txtapellidom"]
    cuenta=request.POST["txtcuenta"]
    apellidop=request.POST["txtapellidop"]
    guardarcliente=Cliente.objects.create(codigo=codigo,nombre=nombre,telefono=telefono,direccion=direccion,apellidom=apellidom,cuenta=cuenta,apellidop=apellidop)
    return redirect("Cliente")

def seleccionarCliente(request,codigo):
    negocio=Cliente.objects.get(codigo=codigo)
    return render(request,"editarCliente.html",{"misclientes":negocio})

def editarCliente(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["txttelefono"]
    direccion=request.POST["txtdireccion"]
    apellidom=request.POST["txtapellidom"]
    cuenta=request.POST["txtcuenta"]
    apellidop=request.POST["txtapellidop"]
    negocio=Cliente.objects.get(codigo=codigo)
    negocio.nombre=nombre
    negocio.telefono=telefono
    negocio.direccion=direccion
    negocio.apellidom=apellidom
    negocio.cuenta=cuenta
    negocio.apellidop=apellidop
    negocio.save()
    return redirect("Cliente")

def borrarCliente(request,codigo):
    materia=Cliente.objects.get(codigo=codigo)
    materia.delete()
    return redirect("Cliente")