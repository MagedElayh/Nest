# Generated by Django 3.2.12 on 2022-02-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_remove_product_product_image_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image_sale',
            field=models.ImageField(blank=True, null=True, upload_to='products/imgs/', verbose_name='Product Image Sale'),
        ),
    ]