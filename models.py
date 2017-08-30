from django.db import models


class ContactInfo(models.Model):
    mobileNumber = models.PositiveIntegerField()
    phoneNumber = models.PositiveIntegerField()
    emailID = models.EmailField(max_length=50)


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    landmark = models.CharField(max_length=20, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)


class Customer(ContactInfo, Address):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
