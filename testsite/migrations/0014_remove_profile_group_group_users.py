# Generated by Django 4.2 on 2024-02-29 14:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testsite', '0013_alter_profile_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='group',
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
