# Generated by Django 4.2.7 on 2023-11-24 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_alter_client_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
    ]
