# Generated by Django 3.2.5 on 2021-11-21 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elibraryapp', '0004_books_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='book',
            new_name='book_file',
        ),
    ]