# Generated by Django 3.2.13 on 2023-12-20 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_auto_20231220_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
    ]
