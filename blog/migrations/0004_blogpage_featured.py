# Generated by Django 4.2.1 on 2024-01-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_blogpage_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="featured",
            field=models.BooleanField(default=False),
        ),
    ]
