# Generated by Django 3.0.5 on 2020-05-02 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_orders', '0004_foodimages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FoodImages',
            new_name='FoodImage',
        ),
        migrations.RenameModel(
            old_name='FoodItems',
            new_name='FoodItem',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='OrderDetails',
            new_name='OrderDetail',
        ),
    ]