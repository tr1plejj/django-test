# Generated by Django 4.2 on 2024-02-29 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0004_rename_lesson_product_lessons_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='lessons',
            new_name='included_lessons',
        ),
    ]
