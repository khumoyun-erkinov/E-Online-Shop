from django.urls import path, include
from .views import CategoryListCreate, CategoryRetrieveUpdateDelete, \
    ProductListCreate, ProductRetrieveUpdateDelete

urlpatterns = [
    path('category/', CategoryListCreate.as_view(), name='author_list'),
    path('category/<pk>/', CategoryRetrieveUpdateDelete.as_view(), name='category_detail'),
    path('product/', ProductListCreate.as_view(), name='product_list'),
    path('product/<pk>/', ProductRetrieveUpdateDelete.as_view(), name='product_detail'),

]
