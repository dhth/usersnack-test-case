# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class Order(models.Model):
    """
    Source of truth for orders.
    """

    status = models.CharField(max_length=50, default="initiated")
    user_name = models.CharField(max_length=255)
    user_address = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class FoodItem(models.Model):
    """
    Stores all food items offered by the store.
    TODO: Add a relationship for item_type instead of CharField.
    """

    name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    active_in_menu = models.BooleanField(default=True)


class FoodImage(models.Model):
    """
    Maps foods to their images.
    """

    food_id = models.ForeignKey(
        FoodItem, on_delete=models.PROTECT, related_name="images"
    )
    img_file = models.CharField(max_length=100)


class OrderDetail(models.Model):
    """
    Stores each food component for an order, along with quantity for
    each.
    """

    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    food_item = models.ForeignKey(FoodItem, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
