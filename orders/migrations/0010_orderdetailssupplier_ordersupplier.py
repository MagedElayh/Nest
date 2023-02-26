# Generated by Django 3.2.12 on 2022-03-11 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0052_alter_product_prdslug'),
        ('orders', '0009_auto_20220311_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_client', models.EmailField(blank=True, max_length=250, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('sub_total', models.CharField(blank=True, max_length=50, null=True)),
                ('discount', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.CharField(max_length=50)),
                ('tracking_no', models.CharField(blank=True, max_length=50, null=True)),
                ('rpt_cache', models.URLField(blank=True, null=True)),
                ('weight', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='WEIGHT')),
                ('is_finished', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('Underway', 'Underway'), ('COMPLETE', 'COMPLETE'), ('Refunded', 'Refunded')], default='PENDING', max_length=13)),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.coupon')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='OrderDetailsSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
                ('size', models.CharField(blank=True, max_length=10, null=True)),
                ('weight', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='WEIGHT')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]