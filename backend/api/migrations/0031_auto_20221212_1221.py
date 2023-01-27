# Generated by Django 3.2 on 2022-12-12 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_alter_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='cover',
            field=models.ImageField(upload_to='authors'),
        ),
        migrations.AlterField(
            model_name='author',
            name='image1',
            field=models.ImageField(upload_to='authors'),
        ),
        migrations.AlterField(
            model_name='author',
            name='image2',
            field=models.ImageField(upload_to='authors'),
        ),
        migrations.AlterField(
            model_name='author',
            name='image3',
            field=models.ImageField(upload_to='authors'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to='books'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='books'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cover',
            field=models.ImageField(upload_to='categories'),
        ),
    ]
