# Generated by Django 3.2.13 on 2023-12-20 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import files.models
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shops', '0004_remove_product_photo'),
        ('files', '0002_alter_file_field_to_image_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('file', models.ImageField(upload_to=files.models.get_file_upload_path)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shops.product')),
            ],
            options={
                'verbose_name': "product's photo",
                'verbose_name_plural': "product's photos",
            },
        ),
    ]
