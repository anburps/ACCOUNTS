from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

class MyUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.site = '127.0.0.1:8000'
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.model(email=email,is_staff=True, is_superuser=True, **extra_fields)
        user.site = '127.0.0.1:8000'
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    display_name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(unique=True,blank=True, null=True,unique=True)
    uid = models.CharField(max_length=100,blank=True, null=True,unique=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    phone = models.CharField(max_length=100,blank=True, null=True)
    is_staff = models.BooleanField(default=False,default=False)
    is_superuser = models.BooleanField(default=False,default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    device_token = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    additional_data = models.JSONField(default=dict,blank=True, help_text="Additional Data")

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email