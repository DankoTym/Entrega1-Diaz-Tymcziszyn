from socket import fromshare
from django import forms

class ProductosFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    articulo = forms.IntegerField()


class ContactoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()


class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
