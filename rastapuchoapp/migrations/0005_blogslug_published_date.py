# Generated by Django 3.0.8 on 2021-02-01 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rastapuchoapp', '0004_blogslug_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogslug',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]