# Generated by Django 3.2.16 on 2024-02-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='img',
            field=models.FileField(max_length=128, upload_to='city2', verbose_name='LOGO'),
        ),
    ]
