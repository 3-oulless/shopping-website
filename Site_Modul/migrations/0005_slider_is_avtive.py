# Generated by Django 4.2 on 2023-04-23 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_Modul', '0004_slider_alter_footerlink_footer_link_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='is_avtive',
            field=models.BooleanField(default=False, verbose_name='فعال با غیر فعال'),
        ),
    ]
