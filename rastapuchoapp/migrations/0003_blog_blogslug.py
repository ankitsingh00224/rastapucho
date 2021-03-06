# Generated by Django 3.0.8 on 2021-02-01 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rastapuchoapp', '0002_recentcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSlug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_title', models.CharField(max_length=500)),
                ('slug_content', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'slugs',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('slug', models.CharField(default=1, max_length=500)),
                ('slug_title', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='rastapuchoapp.BlogSlug')),
            ],
        ),
    ]
