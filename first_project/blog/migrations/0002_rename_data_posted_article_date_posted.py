# Generated by Django 4.1 on 2022-09-04 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="data_posted",
            new_name="date_posted",
        ),
    ]