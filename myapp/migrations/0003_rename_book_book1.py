# Generated by Django 5.0.1 on 2024-01-26 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_publishedate_book_publisheddate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Book1',
        ),
    ]