from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView,DeleteView,UpdateView

from products.models import Products,Category
from products.forms import ProductForm,CategoryForm
# Create your views here.

def create_product(request):
    if request.method == 'GET':
        context={
            'form':ProductForm()
        }
        return render (request,'Productos/create_product.html',context=context)
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Products.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                stock= form.cleaned_data['stock'],
            )
            context = {
                'message':'producto creado exitosamente'
            }
            return render (request,'Productos/create_product.html',context=context)
        else:
            context = {
                'form_errors': form.errors,
            }
        return render (request,'Productos/create_product.html',context=context)


@login_required
def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Products.objects.filter(name__icontains =search)
    else:
        products = Products.objects.all()
    context={
        'products': products,
    }
    return render (request,'Productos/list_products.html',context=context)

class ProductUpdateView(UpdateView):
    model = Products
    template_name = 'Productos/update_product.html'
    fields = '__all__'
    success_url= '/products/list_products/'

class ProductDeleteView(DeleteView):
    model = Products
    template_name= 'Productos/delete_product.html'
    success_url = '/products/list_products/'


class CategoryListView(LoginRequiredMixin,ListView):
    model = Category
    template_name = 'Categorias/list_categories.html'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'Categorias/create_category.html'
    fields = '__all__'
    success_url = '/products/list_categories/'

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'Categorias/update_category.html'
    fields = '__all__'
    success_url = '/products/list_categories/'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name= 'Categorias/delete_category.html'
    success_url= '/products/list_categories/'
