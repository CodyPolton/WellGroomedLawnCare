# Generated by Django 3.0 on 2020-01-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200103_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobexpense',
            name='date_purchased',
            field=models.DateField(null=True),
        ),
    ]