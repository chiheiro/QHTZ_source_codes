# Generated by Django 2.2.7 on 2019-11-08 04:06

from django.db import migrations, models
import imagestorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indeximages',
            name='image',
            field=models.ImageField(blank=True, storage=imagestorage.storage.ImageStorage(), upload_to='images/', verbose_name='选择图片'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(blank=True, storage=imagestorage.storage.ImageStorage(), upload_to='images/', verbose_name='选择图片'),
        ),
    ]
