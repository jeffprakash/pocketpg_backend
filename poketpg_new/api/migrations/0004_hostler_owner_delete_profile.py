# Generated by Django 4.1.3 on 2022-12-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_remove_profile_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="hostler",
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
                ("name", models.TextField()),
                ("age", models.IntegerField(blank=True, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("college", models.TextField(blank=True, null=True)),
                ("password", models.CharField(blank=True, max_length=100, null=True)),
                ("phno", models.IntegerField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="owner",
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
                ("name", models.TextField()),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("companyname", models.TextField(blank=True, null=True)),
                ("password", models.CharField(blank=True, max_length=100, null=True)),
                ("location", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]