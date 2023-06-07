# Generated by Django 4.1.7 on 2023-04-05 18:59

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0005_product_external_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=5, default=Decimal("0"), max_digits=10
            ),
        ),
    ]