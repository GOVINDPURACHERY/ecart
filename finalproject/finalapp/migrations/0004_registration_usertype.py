# Generated by Django 4.2.1 on 2023-05-26 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0003_remove_registration_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='usertype',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
