from django.db import models
from django.contrib.auth.models import AbstractUser

#My Database Tables

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=50)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.email
    
class user_table(models.Model):
    mfname = models.CharField(max_length=50)
    mmname = models.CharField(max_length=50)
    mlname = models.CharField(max_length=50)
    mdob = models.DateField(max_length=11)
    mnationality = models.CharField(max_length=30)
    moccupation = models.CharField(max_length=30)
    mincome = models.PositiveBigIntegerField()
    mwork = models.TextField()
    mstate = models.CharField(max_length=50)
    ffname = models.CharField(max_length=50)
    fmname = models.CharField(max_length=50)
    flname = models.CharField(max_length=50)
    fdob = models.DateField(max_length=10)
    fnationality = models.CharField(max_length=30)
    foccupation = models.CharField(max_length=30)
    fincome = models.PositiveBigIntegerField()
    fwork = models.TextField()
    fstate = models.CharField(max_length=50)
    bchild = models.PositiveSmallIntegerField()
    achild = models.PositiveSmallIntegerField()
    uaddress = models.TextField()
    upincode = models.PositiveBigIntegerField()
    uemail = models.EmailField(null=True,max_length=70)
    uphone = models.CharField(max_length=10)
    def __str__(self):
        return self.uemail
    
class agency_table(models.Model):
    aname = models.CharField(max_length=255)
    aemail = models.EmailField(max_length=70)
    aphone = models.CharField(max_length=10)
    aaddress = models.TextField()
    astate = models.CharField(max_length=50)
    apincode = models.PositiveBigIntegerField()
    mzerotofive = models.PositiveSmallIntegerField()
    mfivetoten = models.PositiveSmallIntegerField()
    mtentofifteen = models.PositiveSmallIntegerField()
    mabovefifteen = models.PositiveSmallIntegerField()
    fzerotofive = models.PositiveSmallIntegerField()
    ffivetoten = models.PositiveSmallIntegerField()
    ftentofifteen = models.PositiveSmallIntegerField()
    fabovefifteen = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.aemail