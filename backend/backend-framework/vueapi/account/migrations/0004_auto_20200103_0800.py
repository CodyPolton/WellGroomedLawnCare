# Generated by Django 3.0 on 2020-01-03 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_jobexpense_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobexpense',
            old_name='expense_type',
            new_name='job_expense_type',
        ),
        migrations.AlterField(
            model_name='jobexpense',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
