# Generated by Django 3.2.13 on 2023-12-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_category_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='shops.Category'),
        ),
        migrations.AddField(
            model_name='shop',
            name='allowed_categories',
            field=models.ManyToManyField(to='shops.Category'),
        ),
    ]
