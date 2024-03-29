# Generated by Django 4.1.7 on 2023-06-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0003_bookmark_rating_bookmark_stamp"),
    ]

    operations = [
        migrations.CreateModel(
            name="marker",
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
                ("place", models.CharField(db_column="place", max_length=50)),
                ("parking", models.CharField(db_column="parking", max_length=50)),
                ("address", models.CharField(db_column="address", max_length=50)),
                ("lat", models.CharField(db_column="lat", max_length=50)),
                ("lng", models.CharField(db_column="lng", max_length=50)),
            ],
        ),
    ]
