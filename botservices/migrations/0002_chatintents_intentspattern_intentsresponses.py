# Generated by Django 5.0.1 on 2024-02-10 13:23

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("botservices", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatIntents",
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
                ("tag", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="IntentsPattern",
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
                ("pattern", models.CharField(max_length=255)),
                (
                    "parent",
                    modelcluster.fields.ParentalKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="intents_pattern",
                        to="botservices.chatintents",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IntentsResponses",
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
                ("responses", models.CharField(max_length=255)),
                (
                    "parent",
                    modelcluster.fields.ParentalKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="intents_responses",
                        to="botservices.chatintents",
                    ),
                ),
            ],
        ),
    ]