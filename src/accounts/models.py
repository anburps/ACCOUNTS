from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # staff and superuser can login def is_staff and def is_superuser
    def is_staff(self, obj=None,  *args, **kwargs):    
        is_staff = models.BooleanField(default=True)
        is_active = models.BooleanField(default=True)
        is_superuser = models.BooleanField(default=False)
        return is_staff
    
    def is_superuser(self, obj=None,  *args, **kwargs):    
        is_staff = models.BooleanField(default=True)
        is_active = models.BooleanField(default=True)
        is_superuser = models.BooleanField(default=True)
        return is_superuser
    
class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    device_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user