from rest_framework import serializers 
from core.models import User, Product, Order, OrderItem



class UserProdSerializers(serializers.ModelSerializer):
    class Meta:
        model =  User 
        fields = ['id','name','email', 'phone_number', 'role']

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Product 
        fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):
    user_detail = UserProdSerializers(read_only=True, source="user")
    #  = ProductSerializers()
    class Meta:
        model = Order
        fields = '__all__'

class ListOrderSerializers(serializers.ModelSerializer):
    # product = ProductSerializers()
    user_detail = UserProdSerializers(read_only=True,many=False , source="user")
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializers(serializers.ModelSerializer):
    order_detail = OrderSerializers(read_only=True, source="order")

    class Meta: 
        model = OrderItem 
        fields = '__all__'


