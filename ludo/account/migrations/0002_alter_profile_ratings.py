# Generated by Django 4.1 on 2022-08-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ratings',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]