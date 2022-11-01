from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppProyecto.models import Producto, Cliente, Contacto
from AppProyecto.forms import ProductosFormulario, ClienteFormulario, ContactoFormulario


# Create your views here.

def Inicio(self):
    plantilla = loader.get_template('AppProyecto/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

#------Carga de Datos-------------
def productosFormulario(request):
    if request.method == 'POST':
        miFormulario = ProductosFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre = informacion['nombre']
        articulo = informacion['articulo']

        producto = Producto(nombre=nombre, articulo=articulo)
        producto.save()
        return render(request, "AppProyecto/inicio.html")
    else:
        miFormulario = ProductosFormulario()

    return render(request, 'AppProyecto/productosFormulario.html', {'miFormulario':miFormulario})

def contactoFormulario(request):
    if request.method == 'POST':
        miFormulario = ContactoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        email = informacion['email']

        contacto = Contacto(nombre=nombre, apellido=apellido, email=email)
        contacto.save()
        return render(request, "AppProyecto/inicio.html")
    else:
        miFormulario = ContactoFormulario()

    return render(request, 'AppProyecto/contactoFormulario.html', {'miFormulario':miFormulario})

def clientesFormulario(request):
    if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        email = informacion['email']

        cliente = Cliente(nombre=nombre, apellido=apellido, email=email)
        cliente.save()
        return render(request, "AppProyecto/inicio.html")
    else:
        miFormulario = ClienteFormulario()

    return render(request, 'AppProyecto/clienteFormulario.html', {'miFormulario':miFormulario})