from django.db.models.base import Model
from rest_framework import serializers
from petshop.models import Category, Dog, Client, Order


class DogSerializer (serializers.ModelSerializer):
    dog_id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Dog
        fields = ['dog_id','price','category_name','category_id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id','category_name','dog_id']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id','client_name']

class OrderSerializer(serializers.ModelSerializer):
    ''' client_id = serializers.IntegerField()
    dog_id = serializers.IntegerField()
    price = serializers.FloatField()'''
    class Meta:
        model = Order
        fields = ['client_id','dog_id','price']
