# Generated by Django 5.1.3 on 2025-03-12 15:21

import purchase_orders.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='name',
            field=models.CharField(default=purchase_orders.models.generate_name, editable=False, max_length=255, unique=True),
        ),
    ]
