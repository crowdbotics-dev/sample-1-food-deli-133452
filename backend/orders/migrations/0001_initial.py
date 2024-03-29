# Generated by Django 3.2.23 on 2024-03-05 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authentication", "0001_initial"),
        ("restaurants", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("items", models.JSONField()),
                ("special_requests", models.TextField(blank=True, null=True)),
                ("status", models.CharField(max_length=50)),
                ("scheduled_time", models.DateTimeField(blank=True, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_customer",
                        to="authentication.customer",
                    ),
                ),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_restaurant",
                        to="restaurants.restaurant",
                    ),
                ),
            ],
        ),
    ]
