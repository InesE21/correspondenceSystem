# Generated by Django 5.0.9 on 2024-10-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_remove_customer_customertype_customer_customer_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phoneNumber',
            field=models.CharField(max_length=10, unique=True, verbose_name='phone number'),
        ),
    ]