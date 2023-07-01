# Generated by Django 4.2.2 on 2023-06-24 13:54

import uuid

import django.core.validators
from django.db import migrations, models

import account.services


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="ID",
                    ),
                ),
                ("nickname", models.CharField(max_length=120, unique=True)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("name", models.CharField(blank=True, max_length=60, null=True)),
                ("surname", models.CharField(blank=True, max_length=60, null=True)),
                (
                    "img",
                    models.ImageField(
                        blank=True,
                        default=account.services.get_default_user_img_path,
                        null=True,
                        upload_to=account.services.get_custom_user_img_path,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpg"]
                            ),
                            account.services.validate_size_image,
                        ],
                    ),
                ),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("last_login", models.DateTimeField(auto_now=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
