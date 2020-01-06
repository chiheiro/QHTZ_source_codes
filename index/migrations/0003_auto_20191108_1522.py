# Generated by Django 2.2.7 on 2019-11-08 07:22

from django.db import migrations, models
import imagestorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20191108_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_introduction', models.CharField(default='毕业于郑州某大学，自学UI设计，云计算，linux系统管理和python以及一些主流的web框架。其中li    nux系统和python是强项，个人博客：\n', max_length=50, verbose_name='首页关于我')),
                ('image', models.ImageField(blank=True, storage=imagestorage.storage.ImageStorage(), upload_to='images/', verbose_name='选择图片')),
                ('imagename', models.CharField(default='未命名图片', max_length=20, verbose_name='图片名')),
                ('upldtime', models.DateField(auto_now=True, verbose_name='上传时间')),
                ('chatime', models.DateField(auto_now=True, verbose_name='最后更改时间')),
            ],
            options={
                'verbose_name': '首页信息',
                'verbose_name_plural': '首页信息',
                'db_table': 'index',
            },
        ),
        migrations.DeleteModel(
            name='IndexImages',
        ),
    ]