# Generated by Django 3.2 on 2022-06-03 03:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_book_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='desription',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 3, 8, 21, 12, 51378)),
        ),
    ]
