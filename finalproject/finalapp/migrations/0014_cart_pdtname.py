# Generated by Django 4.2.1 on 2023-06-07 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0013_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='pdtname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
