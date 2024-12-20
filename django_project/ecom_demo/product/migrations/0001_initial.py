# Generated by Django 5.1 on 2024-10-28 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subcat', '0002_alter_subcategories_cat_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=100, unique=True)),
                ('actual_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=3)),
                ('image', models.ImageField(upload_to='images/')),
                ('sub_cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='subcat.subcategories')),
            ],
        ),
    ]
