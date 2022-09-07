from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Basket, Customer


@receiver(post_save, sender=Basket)
def create_customer_and_basket(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(basket=instance, name='example')
