# Generated by Django 4.1 on 2022-09-08 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("API", "0002_alter_book_authors_alter_book_categories_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="published_data",
            new_name="published_date",
        ),
    ]
