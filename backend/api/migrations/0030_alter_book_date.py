# Generated by Django 3.2 on 2022-06-13 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20220608_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
