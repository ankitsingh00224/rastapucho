# Generated by Django 3.1.3 on 2021-02-03 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rastapuchoapp', '0011_auto_20210202_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogslug',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 15, 44, 37, 939610), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='card',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 15, 44, 37, 937563), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 2, 3, 15, 44, 37, 940558)),
        ),
        migrations.AlterField(
            model_name='review',
            name='your_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
