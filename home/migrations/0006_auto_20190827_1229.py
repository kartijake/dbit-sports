# Generated by Django 2.2.1 on 2019-08-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_club_image_clubs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club_image',
            name='image',
            field=models.ImageField(upload_to='clubs/images'),
        ),
    ]
