# Generated by Django 4.2.2 on 2023-07-08 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_alter_account_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="slug",
            field=models.SlugField(default=" "),
            preserve_default=False,
        ),
    ]
