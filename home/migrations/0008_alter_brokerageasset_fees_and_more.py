# Generated by Django 5.0.1 on 2024-01-14 16:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_alter_brokerageasset_fees_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brokerageasset",
            name="fees",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=10,
                null=True,
                verbose_name="Custos (R$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="for_purchase_exchange_sell",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                default=0,
                max_digits=10,
                null=True,
                verbose_name="Para compra, câmbio de venda (R$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="for_sale_exchange_purchase",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                default=0,
                max_digits=10,
                null=True,
                verbose_name="Para venda, câmbio de compra (R$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="origin_in_foreign_currency",
            field=models.DecimalField(
                blank=True,
                decimal_places=10,
                default=0,
                max_digits=20,
                null=True,
                verbose_name="Origem moeda estrangeira (US$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="origin_in_national_currency",
            field=models.DecimalField(
                blank=True,
                decimal_places=10,
                default=0,
                max_digits=20,
                null=True,
                verbose_name="Origem moeda nacional (US$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="purchase_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=10,
                default=0,
                max_digits=20,
                null=True,
                verbose_name="Valor da compra (R$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="sell_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=10,
                default=0,
                max_digits=20,
                null=True,
                verbose_name="Valor da venda (R$)",
            ),
        ),
    ]
