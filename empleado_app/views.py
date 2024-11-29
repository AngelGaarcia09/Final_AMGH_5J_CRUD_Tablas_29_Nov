from django.shortcuts import render,redirect
from.models import Empleado
# Create your views here.

def inicio_vistaEmpleado(request):
    losnegocios=Empleado.objects.all()

    return render(request,"gestionarNegocio.html",{"misnegocios":losnegocios})


def registrarEmpleado(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    puesto=request.POST["txtpuesto"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    email=request.POST["txtemail"]
    apellido=request.POST["txtapellido"]
    guardarempleado=Empleado.objects.create(codigo=codigo,nombre=nombre,puesto=puesto,direccion=direccion,telefono=telefono,email=email,apellido=apellido)
    return redirect("Empleado")

def seleccionarEmpleado(request,codigo):
    negocio=Empleado.objects.get(codigo=codigo)
    return render(request,"editarNegocio.html",{"misnegocios":negocio})

def editarEmpleado(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    puesto=request.POST["txtpuesto"]
    direccion=request.POST["txtpuesto"]
    telefono=request.POST["txttelefono"]
    email=request.POST["txtemail"]
    apellido=request.POST["txtapellido"]
    negocio=Empleado.objects.get(codigo=codigo)
    negocio.nombre=nombre
    negocio.puesto=puesto
    negocio.direccion=direccion
    negocio.telefono=telefono
    negocio.email=email
    negocio.apellido=apellido
    negocio.save()
    return redirect("Empleado")

def borrarEmpleado(request,codigo):
    materia=Empleado.objects.get(codigo=codigo)
    materia.delete()
    return redirect("Empleado")