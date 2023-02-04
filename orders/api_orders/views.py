from rest_framework import generics
from .serializers import OrderItemSerializer, OrderSerialaizer
from orders.models import Order, OrderItem


# Create your views here

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerialaizer


class OrderRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerialaizer


class OrderItemCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemRetrieveUpdateDelete(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
