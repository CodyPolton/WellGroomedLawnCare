from django.db import models

# Create your models here.
class Account(models.Model):
    accountid = models.IntegerField()
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    phone_no = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    auto_invoice = models.BooleanField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

