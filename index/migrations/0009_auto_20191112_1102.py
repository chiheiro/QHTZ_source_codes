# Generated by Django 2.2.7 on 2019-11-12 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20191112_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indeximages',
            name='show',
            field=models.BooleanField(default=True, verbose_name='是否在首页展示'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='show',
            field=models.BooleanField(default=True, verbose_name='是否在首页展示'),
        ),
    ]
