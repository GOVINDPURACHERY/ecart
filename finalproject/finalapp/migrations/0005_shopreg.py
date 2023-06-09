# Generated by Django 4.2.1 on 2023-05-30 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0004_registration_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='shopreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=100, null=True)),
                ('ownername', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.IntegerField(max_length=100, null=True)),
                ('usertype', models.CharField(default='shop', max_length=100, null=True)),
                ('industry', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
