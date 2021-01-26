# Generated by Django 3.1.3 on 2021-01-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tannu', models.CharField(max_length=100)),
                ('mannu', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='images')),
                ('urls1', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TopCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title2', models.CharField(max_length=100)),
                ('image2', models.ImageField(upload_to='images')),
                ('description2', models.TextField()),
                ('urls2', models.CharField(max_length=250)),
            ],
        ),
    ]