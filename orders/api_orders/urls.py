from django.urls import path
from .views import OrderItemCreateView, OrderListCreateView, OrderItemRetrieveUpdateDelete, OrderRetrieveUpdateDelete

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='orders_list'),
    path('orders/<pk>/', OrderRetrieveUpdateDelete.as_view(), name='orders_pk'),
    path('orderitem/', OrderItemCreateView.as_view(), name='orderitem_list'),
    path('orderitem/<pk>/', OrderItemRetrieveUpdateDelete.as_view(), name='orderitem_pk')
]
