from django.db import models

# Create your models here.

class Dog (models.Model):
    dog_id = models.IntegerField()
    price = models.CharField(max_length=10)
    category_name = models.TextField(max_length=250)
    category_id = models.IntegerField()

   

    #client = models.ForeignKey('auth.Client', related_name='dogs', on_delete=models.CASCADE)
class Category (models.Model):
    category_id = models.IntegerField()
    category_name = models.TextField(max_length=250)
    dog_id = models.IntegerField()

class Client(models.Model):
    client_id = models.IntegerField()
    client_name = models.TextField(max_length=250)

class Order (models.Model):
    client_id = models.IntegerField()
    dog_id = models.IntegerField()
    price = models.CharField(max_length=10)

    #client_id = models.ForeignKey('auth.Client', related_name='petshop', on_delete=models.CASCADE)