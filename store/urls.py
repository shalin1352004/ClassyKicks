from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('add-brand/', views.add_brand, name='add_brand'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
