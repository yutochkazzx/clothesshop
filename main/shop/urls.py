from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.product_create, name='product_create'),
    path('<int:id>/<slug:slug>/delete/', views.product_delete, name='product_delete'),
    path('<slug:category_slug>/', views.product_list, name='product_list_bycat'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
