# Generated by Django 4.2.4 on 2023-08-26 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_product_count39_product_count40_product_count41'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
    ]
