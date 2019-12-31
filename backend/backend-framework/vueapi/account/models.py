from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Account(models.Model):
    accountid = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255)
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    phone_no = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=255, blank=True)
    auto_invoice = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'accounts'
        ordering = ['accountid']

class Yard(models.Model):
    yardid = models.AutoField(primary_key=True)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    mow_price = models.DecimalField( max_digits=6, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'yards'
        ordering = ['yardid']

class JobType(models.Model):
    job_typeid = models.AutoField(primary_key=True)
    job_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'job_types'
        ordering = 'job_typeid'

class Job(models.Model):
    jobid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    job_type = models.ForeignKey('JobType', on_delete=models.CASCADE)
    date_completed = models.DateTimeField( blank=True)
    job_total = models.DecimalField( max_digits=10, decimal_places=2)
    billed = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'jobs'
        ordering = 'jobid'



