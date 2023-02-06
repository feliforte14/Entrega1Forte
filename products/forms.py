from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    detalle = forms.CharField(max_length=500)
    price = forms.FloatField()
    stock = forms.BooleanField(required=False)

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100)