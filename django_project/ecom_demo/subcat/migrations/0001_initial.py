# Generated by Django 5.1 on 2024-10-16 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_rename_service_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.categories')),
            ],
        ),
    ]