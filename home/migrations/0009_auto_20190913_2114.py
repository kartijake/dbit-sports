# Generated by Django 2.2.1 on 2019-09-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190910_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club_image',
            name='image',
            field=models.ImageField(upload_to='images/clubs/'),
        ),
    ]
