# Generated by Django 4.1.6 on 2023-07-20 12:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0003_fencedfield"),
    ]

    operations = [
        migrations.AddField(
            model_name="fencedfield",
            name="timestamp",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
