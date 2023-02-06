from django import forms

class ClientForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    detalle = forms.CharField(max_length=500)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=50)
