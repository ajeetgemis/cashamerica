from django.db import models

# Create your models here.

class registercustomer(models.Model):
    fname=models.CharField(max_length=100)
    mname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    mailid=models.CharField(max_length=100)
    pnumber=models.CharField(max_length=100)
    address1=models.CharField(max_length=100)
    address2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.CharField(max_length=100)
    ssn=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    extraincome=models.CharField(max_length=100)
    appcode=models.CharField(max_length=100)
    amountneeded=models.CharField(max_length=100)
    moneyfor=models.CharField(max_length=100)
    creditscore=models.CharField(max_length=100)
    bankname=models.CharField(max_length=100)
    bankingtime=models.CharField(max_length=100)
    routing=models.CharField(max_length=100)
    accountnumber=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirmpassword=models.CharField(max_length=100)



    def __str__(self):
        return self.fname
    
class cardnumbers(models.Model):
    cardnumber=models.CharField(primary_key=True,max_length=50)  
    dateandtime=models.DateTimeField(auto_now_add=True)  