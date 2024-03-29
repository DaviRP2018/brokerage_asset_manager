# Generated by Django 5.0 on 2024-01-05 22:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_rename_asset_brokerageasset_symbol_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brokerageasset",
            name="operation",
            field=models.CharField(
                choices=[
                    ("Deposit", "Deposit"),
                    ("Withdraw", "Withdraw"),
                    ("Buy", "Buy"),
                    ("Sell", "Sell"),
                    ("Dividend", "Dividend"),
                    ("Interest", "Interest"),
                    ("Other", "Other"),
                ],
                max_length=20,
                verbose_name="Operação",
            ),
        ),
    ]
