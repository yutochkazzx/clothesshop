from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    """
    Форма создания товара пользователем.
    Поле владельца заполняется во вьюхе.
    """

    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'slug',
            'image',
            'description',
            'price',
            'size',
            'discount_percentage',
            'available',
        ]

