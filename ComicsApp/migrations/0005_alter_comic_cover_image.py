# Generated by Django 4.2.4 on 2023-09-08 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComicsApp', '0004_comic_cover_image_delete_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='cover_image',
            field=models.ImageField(upload_to='covers'),
        ),
    ]
