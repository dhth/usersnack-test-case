# Generated by Django 3.0.5 on 2020-05-03 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_orders', '0005_auto_20200502_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='initiated', max_length=50),
        ),
    ]