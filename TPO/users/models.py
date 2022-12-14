# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
import uuid
import re
from django.core.exceptions import ValidationError
class User(AbstractUser):
    username = models.CharField(max_length= 50,unique=True)
    is_customer = models.BooleanField(default=False)
    is_store = models.BooleanField(default=False)
    is_delivery = models.BooleanField(default=False)
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    location = models.CharField( max_length=50)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    phone_number = models.CharField(max_length=16)
    pattern = re.compile(r'^\+\d{8,15}$')

    def clean(self):
        if not self.pattern.match(self.phone_number):
            raise ValidationError('Invalid phone number')
    def __str__(self):
        return self.get_username()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    def __str__(self):
        return self.user.get_username()

class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user.get_username()

class Delivery(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user.username
