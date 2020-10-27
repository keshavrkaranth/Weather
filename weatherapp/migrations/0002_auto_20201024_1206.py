# Generated by Django 3.1.2 on 2020-10-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='icon',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='temprature',
            field=models.FloatField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]