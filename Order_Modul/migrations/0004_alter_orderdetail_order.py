# Generated by Django 4.2 on 2023-06-27 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order_Modul', '0003_alter_order_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='Order_Modul.order', verbose_name='سبد خرید'),
        ),
    ]
