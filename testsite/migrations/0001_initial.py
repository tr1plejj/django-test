# Generated by Django 4.2 on 2024-02-29 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=64)),
                ('is_opened', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=64)),
                ('video_url', models.URLField()),
            ],
            options={
                'db_table': 'lesson',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=64)),
                ('product_name', models.CharField(max_length=64)),
                ('start_time', models.DateTimeField()),
                ('max_users_in_group', models.IntegerField()),
                ('min_users_in_group', models.IntegerField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=256)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testsite.group')),
                ('purchased_products', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testsite.lesson')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testsite.product'),
        ),
        migrations.AddField(
            model_name='group',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testsite.product'),
        ),
    ]
