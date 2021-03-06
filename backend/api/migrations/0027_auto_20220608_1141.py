# Generated by Django 3.2 on 2022-06-08 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_book_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.GenericIPAddressField()),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 11, 41, 17, 450637)),
        ),
        migrations.AddField(
            model_name='book',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='api.IPAddress'),
        ),
    ]
