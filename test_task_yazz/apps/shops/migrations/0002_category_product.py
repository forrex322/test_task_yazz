# Generated by Django 3.2.13 on 2023-12-20 19:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name of category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=150, verbose_name='Name of product')),
                ('description', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(500)], verbose_name='Description of product')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price in uah')),
                ('photo', models.ImageField(upload_to='product_photos/', verbose_name='Photo of product')),
                ('keywords', models.CharField(max_length=150, verbose_name='Keywords for product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shops.shop', verbose_name='Shop')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]