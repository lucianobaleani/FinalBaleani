# Generated by Django 4.2.4 on 2023-09-08 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComicsApp', '0003_alter_avatar_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='cover_image',
            field=models.ImageField(default='undefined.png', upload_to='covers'),
        ),
        migrations.DeleteModel(
            name='Cover',
        ),
    ]
