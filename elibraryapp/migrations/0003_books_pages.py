# Generated by Django 3.2.5 on 2021-11-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibraryapp', '0002_books_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='pages',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
