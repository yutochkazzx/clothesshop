from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',) }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'createddate', 'updated']
    list_filter = ['available', 'createddate', 'updated', 'category']
    list_editable  = ['price', 'available']
    prepopulated_fields = {'slug' : ('name', ) } 