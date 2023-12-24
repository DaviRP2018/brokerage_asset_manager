# Generated by Django 4.2.8 on 2023-12-24 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("history", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("quantity", models.IntegerField()),
                ("live_foreign_value", models.FloatField()),
                ("value", models.FloatField()),
                ("average_buy_price", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="StockIncome",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("quantity", models.IntegerField()),
                ("foreign_value", models.FloatField()),
                ("foreign_fee", models.FloatField()),
                ("exchange_value", models.FloatField()),
                (
                    "history",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="history.history",
                    ),
                ),
            ],
        ),
    ]