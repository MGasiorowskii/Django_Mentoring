from django.db import models
from django.utils import timezone


class Basket(models.Model):
    shopping_list = models.TextField()


class Customer(models.Model):
    name = models.CharField(max_length=50)
    registration_date = models.DateTimeField(default=timezone.now)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
