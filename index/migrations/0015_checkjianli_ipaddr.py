# Generated by Django 2.2.7 on 2019-11-26 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_auto_20191126_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkjianli',
            name='ipaddr',
            field=models.CharField(default='127.0.0.1', max_length=15, verbose_name='访问者IP'),
        ),
    ]
