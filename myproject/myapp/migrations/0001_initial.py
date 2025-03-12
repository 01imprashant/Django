# Generated by Django 5.1.7 on 2025-03-08 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myapp_variety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='myapp/')),
                ('date', models.DateTimeField(default='timezone.now')),
                ('type', models.CharField(choices=[('W', 'WHATSAPP'), ('I', 'INSTAGRAM'), ('F', 'FACEBOOK'), ('A', 'AMAZON'), ('Z', 'ZEPTO')], max_length=2)),
            ],
        ),
    ]
