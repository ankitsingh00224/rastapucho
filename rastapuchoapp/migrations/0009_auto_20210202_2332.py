# Generated by Django 3.1.3 on 2021-02-02 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rastapuchoapp', '0008_auto_20210202_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogslug',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 23, 32, 18, 16713), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='card',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]