# Generated by Django 3.0 on 2020-01-01 22:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accountid', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=255)),
                ('l_name', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('phone_no', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('auto_invoice', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'accounts',
                'ordering': ['accountid'],
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('job_typeid', models.AutoField(primary_key=True, serialize=False)),
                ('job_type', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'job_types',
                'ordering': ['job_typeid'],
            },
        ),
        migrations.CreateModel(
            name='Yard',
            fields=[
                ('yardid', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('mow_price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
            options={
                'db_table': 'yards',
                'ordering': ['yardid'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('jobid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('job_type', models.CharField(max_length=255)),
                ('date_completed', models.DateTimeField(null=True)),
                ('job_total', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('billed', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('yard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Yard')),
            ],
            options={
                'db_table': 'jobs',
                'ordering': ['jobid'],
            },
        ),
    ]