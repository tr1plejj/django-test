# Generated by Django 4.2 on 2024-03-01 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testsite', '0017_alter_group_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='to_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='testsite.product'),
        ),
        migrations.AlterField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='included_lessons',
            field=models.ManyToManyField(related_name='lessons', to='testsite.lesson'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='groups', to='testsite.group'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='purchased_products',
            field=models.ManyToManyField(blank=True, related_name='products', to='testsite.product'),
        ),
    ]
