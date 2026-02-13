from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Аутентификация и регистрация
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # Корзина
    path('cart/', include('cart.urls')),
    # Основной магазин
    path('', include('shop.urls', namespace='main')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
