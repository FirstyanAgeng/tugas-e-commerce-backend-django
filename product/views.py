from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializers, OrderSerializers, OrderItemSerializers, ListOrderSerializers
from core.models import Product, Order, OrderItem, User   
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ListOrderViewSet(viewsets.ModelViewSet):
    serializer_class = ListOrderSerializers
    queryset = Order.objects.all()

class CreateOrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductSerializers
            authentication_classes = [TokenAuthentication]
            permission_classes = [IsAuthenticated]
        else:
            return ProductSerializers

class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializers 
    queryset = OrderItem.objects.all()

