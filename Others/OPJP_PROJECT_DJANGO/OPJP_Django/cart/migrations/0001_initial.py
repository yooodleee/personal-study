# Generated by Django 5.1.3 on 2025-01-08 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.account",
                    ),
                ),
                (
                    "books",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="books.books"
                    ),
                ),
            ],
            options={
                "db_table": "cart",
            },
        ),
    ]
