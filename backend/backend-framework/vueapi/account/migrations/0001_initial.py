# Generated by Django 3.0.1 on 2019-12-27 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountid', models.IntegerField()),
                ('f_name', models.CharField(max_length=255)),
                ('l_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('phone_no', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=255)),
                ('auto_invoice', models.BooleanField()),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
            ],
        ),
    ]
