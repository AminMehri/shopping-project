# Generated by Django 3.2 on 2022-06-08 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20220608_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ipaddress',
            old_name='ipaddress',
            new_name='ip_address',
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 11, 57, 57, 43091)),
        ),
    ]
