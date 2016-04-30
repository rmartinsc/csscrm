from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.
class Company(models.Model):
    company_name=models.CharField(max_length=100)
    company_code=models.CharField(max_length=10, primary_key=True)
    company_address=models.ForeignKey('Address',on_delete=models.CASCADE)
    company_industry=models.CharField(max_length=50)
    company_channel=models.CharField(max_length=50)
    company_salesRep=models.CharField(max_length=50)
    company_revenue=models.FloatField()
    company_amountEmp=models.IntegerField()
    company_createdDate = models.DateTimeField(
            blank=True, null=True)
    
    def create(self):
        self.company_createdDate = timezone.now()
        self.save()

    def __str__(self):
        return self.company_name

class Contact(models.Model):
    contact_company=models.ForeignKey('Company', on_delete=models.CASCADE)
    contact_name=models.CharField(max_length=50)
    contact_role=models.CharField(max_length=50)
    contact_phone1=models.CharField(max_length=50)
    contact_phone2=models.CharField(max_length=50)
    contact_email=models.EmailField(max_length=254)
    contact_called=models.NullBooleanField(null=True)
    contact_createdDate = models.DateTimeField(
            blank=True, null=True)
    
    def create(self):
        self.contact_createdDate = timezone.now()
        self.save()
        
    def call(self):
        #here the connection with the VOIP server would happen
        self.contact_called=True
        self.save()

    def __str__(self):
        return self.contact_name

class Call(models.Model):
    call_company=models.ForeignKey('Company',on_delete=models.CASCADE)
    call_contact=models.ForeignKey('Contact',on_delete=models.CASCADE)
    call_date=models.DateTimeField(
            blank=True, null=True)
    call_tries=models.IntegerField()
    call_rightcontact=models.NullBooleanField(null=True)
    call_comments=models.TextField()
    call_fupdate=models.DateTimeField(
            blank=True, null=True)
    call_islead=models.NullBooleanField(null=True)
    call_leadcode=models.CharField(max_length=10)
    call_visitdate=models.DateTimeField(
            blank=True, null=True)
    
    def call(self):
        #here the connection with the VOIP server would happen
        self.call_date=timezone.now()
        self.save()

    def __str__(self):
        return self.call_comments
        
class Address(models.Model):
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150)
    postalcode = models.CharField(max_length=10)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    
    def __unicode__(self):
        return self.line1