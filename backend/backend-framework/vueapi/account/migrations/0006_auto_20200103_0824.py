# Generated by Django 3.0 on 2020-01-03 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200103_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobexpense',
            name='date_purchased',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]