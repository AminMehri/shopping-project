# Generated by Django 3.2 on 2022-06-07 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 7, 21, 29, 29, 35427)),
        ),
    ]
