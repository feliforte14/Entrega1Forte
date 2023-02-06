from django.contrib import admin

from products.models import Products,Category

# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)