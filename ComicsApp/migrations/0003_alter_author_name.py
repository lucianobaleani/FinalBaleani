# Generated by Django 4.2.4 on 2023-09-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComicsApp', '0002_remove_comic_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=70, unique=True),
        ),
    ]
