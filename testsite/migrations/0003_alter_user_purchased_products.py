# Generated by Django 4.2 on 2024-02-29 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0002_remove_lesson_product_product_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='purchased_products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testsite.product'),
        ),
    ]
