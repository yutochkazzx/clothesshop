from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, Product
from .forms import ProductForm


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-createddate')

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(
        request,
        'main/product/list.html',
        {'category': category, 'categories': categories, 'products': products},
    )


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    suggestedproducts = (
        Product.objects.filter(category=product.category, available=True)
        .exclude(id=product.id)[:4]
    )
    return render(
        request,
        'main/product/details.html',
        {
            'product': product,
            'suggestedproducts': suggestedproducts,
        },
    )


@login_required
def product_create(request):
    """
    Создание нового товара пользователем.
    Доступно только авторизованным (привязанным) аккаунтам.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('main:product_detail', id=product.id, slug=product.slug)
    else:
        form = ProductForm()

    return render(request, 'main/product/create.html', {'form': form})


@login_required
def product_delete(request, id, slug):
    """
    Удаление товара.
    Разрешено только пользователю, создавшему этот товар.
    """
    product = get_object_or_404(Product, id=id, slug=slug)

    if product.owner != request.user:
        return HttpResponseForbidden('У вас нет прав для удаления этого товара.')

    if request.method == 'POST':
        product.delete()
        return redirect('main:product_list')

    return render(request, 'main/product/confirm_delete.html', {'product': product})

