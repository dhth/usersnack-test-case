from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Order(models.Model):
    user_name = models.CharField(max_length=255)
    user_address = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    active_in_menu = models.BooleanField(default=True)


class FoodImage(models.Model):
    food_id = models.ForeignKey(FoodItem, on_delete=models.PROTECT)
    img_file = models.CharField(max_length=100)


class OrderDetail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    food_item = models.ForeignKey(FoodItem, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()