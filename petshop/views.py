from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from petshop.models import Dog, Order
from django.views.decorators.csrf import csrf_exempt
from petshop.serializers import DogSerializer,OrderSerializer

# Create your views here.
dogList = []
@api_view(['GET','POST'])
def dog_list(request, format= None):
    """
    List all dogs, or create a new dog.
    """
    if request.method == 'GET':
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        dogList.append(serializer.data[0])
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def dog_detail(request, pk):
    """
    Retrieve, update or delete a dog.
    """
    try:
        dog = Dog.objects.get(pk=pk)
    except Dog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def make_order(request, format= None):
    """
    List all orders, or create a new order.
    """
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        from django.shortcuts import get_object_or_404
        serializer = OrderSerializer(data=request.data)
        dog_id = request.data.get('dog_id')
        dog_obj = get_object_or_404(Dog, dog_id = dog_id)
        if dog_obj.quantity < 1 :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            dog_obj.quantity = dog_obj.quantity - 1
            dog_obj.save(update_fields=['quantity'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)