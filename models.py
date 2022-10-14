from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import *

class CustumModel(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=10)
    phone_is_verify = models.BooleanField(default=False)
    
    objects = UserManager() 
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
  


# Create your models here.
