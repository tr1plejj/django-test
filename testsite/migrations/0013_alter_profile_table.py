# Generated by Django 4.2 on 2024-02-29 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0012_profile_delete_user'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='profile',
            table='extended_user',
        ),
    ]
