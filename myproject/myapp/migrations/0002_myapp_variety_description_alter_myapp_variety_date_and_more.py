# Generated by Django 5.1.7 on 2025-03-09 03:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myapp_variety',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='myapp_variety',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='myapp_variety',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
