# Generated by Django 3.0.5 on 2020-05-02 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_orders', '0003_fooditems_orderdetails_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_file', models.CharField(max_length=100)),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pizza_orders.FoodItems')),
            ],
        ),
    ]
