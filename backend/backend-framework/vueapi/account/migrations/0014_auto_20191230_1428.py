# Generated by Django 3.0.1 on 2019-12-30 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20191228_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='zip_code',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='yard',
            name='zip_code',
            field=models.IntegerField(max_length=5),
        ),
    ]
