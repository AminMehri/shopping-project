# Generated by Django 3.2 on 2022-06-03 04:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 3, 8, 41, 54, 341227)),
        ),
    ]