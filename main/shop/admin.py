from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',) }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'category', 'price', 'price_with_discount_display',
        'available', 'createddate', 'updated', 'size', 'discount_percentage',
    ]
    list_filter = ['available', 'createddate', 'updated', 'category']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description='Цена со скидкой')
    def price_with_discount_display(self, obj):
        if obj.discount_percentage and obj.discount_percentage > 0:
            return f'{obj.discounted_price} ₽ (−{obj.discount_percentage}%)'
        return '—' 