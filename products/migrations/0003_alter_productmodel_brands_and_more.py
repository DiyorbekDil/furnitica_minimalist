# Generated by Django 5.1.2 on 2024-10-22 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productmodel_discount_productimagemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='brands',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.brandmodel', verbose_name='Brands'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='categories',
            field=models.ManyToManyField(related_name='products', to='products.categorymodel', verbose_name='Categories'),
        ),
    ]