# Generated by Django 4.0.2 on 2022-02-11 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_book_s_best_selling'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='s_best_selling',
            new_name='is_best_selling',
        ),
    ]