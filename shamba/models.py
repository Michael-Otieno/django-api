from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# from django.utils.translation import ugettext_lazy as _
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255,null=True,default=None)
    phone_number = models.CharField(max_length=255,null=True,default=None)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    objects = CustomUserManager()

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
        return self.NextOfKin


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
        return self.LandDes


