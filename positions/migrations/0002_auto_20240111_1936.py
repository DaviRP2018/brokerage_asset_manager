# Generated by Django 5.0 on 2024-01-11 22:36
# Coded by Davi

from django.db import migrations


def forwards(apps, schema_editor):
    account_cash_balance = apps.get_model("positions", "AccountCashBalance")
    account_cash_balance(
        total_balance_in_account=0.00,
        balance_in_national_currency=0.00,
        balance_in_foreign_currency=0.00,
        percent_balance_in_foreign_currency=0.00,
    ).save()


def backwards(apps, schema_editor):
    account_cash_balance = apps.get_model("positions", "AccountCashBalance")
    account_cash_balance.objects.last().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("positions", "0001_initial"),
    ]

    operations = [migrations.RunPython(forwards, backwards)]
