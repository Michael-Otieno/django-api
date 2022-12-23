from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255,null=True,default=None)
    phone_number = models.CharField(max_length=255,null=True,default=None)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class LandOwner(models.Model):
    ProofOwnershipDocument = models.FileField(db_column='image_url', blank=True, null=True, upload_to='images/')
    ChiefFirstName = models.CharField(max_length=255)
    ChiefLastName = models.CharField(max_length=255)
    ChiefPhoneNumber = models.CharField(max_length=255)
    ownerIsVerified = models.BooleanField(default=False)
    NextOfKin = models.CharField(max_length=255)
    NextOfKinRelationship = models.CharField(max_length=255)
    NextOfKinIDNumber = models.CharField(max_length=255)
    NextOfKinPhoneNumber = models.CharField(max_length=255)
    NextOfKinEmail = models.CharField(max_length=255)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.UserId


class LandInformation(models.Model):
    LandOwner = models.ForeignKey(LandOwner, on_delete=models.CASCADE)
    LandSize = models.CharField(max_length=255)
    PricePerAcrePerMonth = models.CharField(max_length=255)
    TotalDurationOfLease = models.CharField(max_length=255)
    County = models.CharField(max_length=255)
    SubCounty = models.CharField(max_length=255)
    Town = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    LandDes = models.TextField(max_length=255)

    def __str__(self):
        return self.LandOwner


