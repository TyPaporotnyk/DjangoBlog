# Generated by Django 4.2.2 on 2023-07-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(default="", unique=True),
        ),
    ]
