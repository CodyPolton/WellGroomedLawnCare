from django.db import models

# Create your models here.
class Account(models.Model):
    accountid = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255)
    zip_code = models.IntegerField()
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
    zip_code = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    mow_price = models.DecimalField( max_digits=6, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'yards'
        ordering = ['yardid']


