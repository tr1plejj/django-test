# Generated by Django 4.2 on 2024-02-29 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0008_remove_product_included_groups_group_to_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='to_product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='testsite.product'),
        ),
    ]
