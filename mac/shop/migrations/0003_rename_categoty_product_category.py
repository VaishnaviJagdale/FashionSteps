# Generated by Django 4.1.3 on 2022-12-07 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_categoty_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categoty',
            new_name='category',
        ),
    ]
