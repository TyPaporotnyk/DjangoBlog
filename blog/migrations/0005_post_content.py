# Generated by Django 4.2.2 on 2023-07-08 18:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_tag_post_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="content",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]