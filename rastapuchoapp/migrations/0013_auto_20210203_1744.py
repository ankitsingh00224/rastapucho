# Generated by Django 3.1.3 on 2021-02-03 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rastapuchoapp', '0012_auto_20210203_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogslug',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 17, 44, 32, 574234), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='card',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 17, 44, 32, 574234), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 2, 3, 17, 44, 32, 578250)),
        ),
        migrations.AlterField(
            model_name='review',
            name='your_image',
            field=models.ImageField(blank=True, null=True, upload_to='review'),
        ),
    ]