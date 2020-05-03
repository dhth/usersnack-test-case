# Generated by Django 3.0.5 on 2020-05-02 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_orders', '0002_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('item_type', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('active_in_menu', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('user_address', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pizza_orders.FoodItems')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pizza_orders.Orders')),
            ],
        ),
    ]