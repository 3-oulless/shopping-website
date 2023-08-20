# Generated by Django 4.2 on 2023-06-25 10:53

import Product.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_alter_product_visit_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=Product.models.upload_image_path_gallery, verbose_name='تصویر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'گالری محصول',
                'verbose_name_plural': 'گالری محصولات',
            },
        ),
    ]