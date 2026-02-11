from django.conf import settings


def cart_count(request):
    """Добавляет в шаблоны переменную cart_count — количество товаров в корзине."""
    cart_data = request.session.get(settings.CART_SESSION_ID, {})
    if not isinstance(cart_data, dict):
        cart_data = {}
    count = sum(item.get('quantity', 0) for item in cart_data.values())
    return {'cart_count': count}
