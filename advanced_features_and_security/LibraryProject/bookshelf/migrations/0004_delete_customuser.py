# Generated by Django 5.1.2 on 2024-11-15 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0003_alter_book_options_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
