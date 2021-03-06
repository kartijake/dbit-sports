# Generated by Django 2.2.3 on 2019-07-25 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('data', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Sports')),
            ],
        ),
    ]
