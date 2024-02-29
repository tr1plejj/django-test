# Generated by Django 4.2 on 2024-02-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0006_remove_user_purchased_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='included_groups',
            field=models.ManyToManyField(to='testsite.group'),
        ),
    ]
