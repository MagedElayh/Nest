# Generated by Django 3.2.12 on 2022-02-05 03:17

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_country', models.CharField(max_length=40)),
                ('country_code', models.CharField(max_length=40)),
                ('countries', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'ordering': ('name_country',),
            },
        ),
    ]
