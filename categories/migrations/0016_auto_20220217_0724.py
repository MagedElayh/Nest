# Generated by Django 3.2.12 on 2022-02-17 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0015_alter_maincategory_super_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minicategory',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='main_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.maincategory'),
        ),
    ]
