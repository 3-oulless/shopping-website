# Generated by Django 4.2 on 2023-04-25 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Article_Module', '0005_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='Article_Module.articlecategory', verbose_name='دسته بندی والد'),
        ),
    ]
