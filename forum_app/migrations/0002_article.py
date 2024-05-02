# Generated by Django 5.0.4 on 2024-05-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
            ],
            options={
                "permissions": [("can_publish", "Can publish articles")],
            },
        ),
    ]
