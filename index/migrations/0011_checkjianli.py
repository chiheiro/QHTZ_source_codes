# Generated by Django 2.2.7 on 2019-11-19 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20191119_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckJianli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(max_length=20, verbose_name='访问者类型')),
                ('ex_time', models.DateTimeField(verbose_name='a访问时间')),
            ],
            options={
                'verbose_name': '简历访问记录',
                'verbose_name_plural': '简历访问记录',
                'db_table': 'QHTZ_checkjianli',
            },
        ),
    ]