# Generated by Django 4.1 on 2022-09-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="last_login_failed",
            field=models.DateField(blank=True, null=True),
        ),
    ]
