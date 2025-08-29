from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

#Usuario customizado
class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    cpf = models.CharField(max_length=12, unique=True)
    rg = models.CharField(max_length=12, unique=True)
    birth_date = models.DateField()
    address_country = models.CharField(max_length=150)
    address_state = models.CharField(max_length=150)
    address_city = models.CharField(max_length=150)
    address_district = models.CharField(max_length=150)
    address_street = models.CharField(max_length=150)
    address_zip_code = models.CharField(max_length=15)
    address_number = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    photo = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'cpf', 'rg', 'birth_date', 
                       'address_country', 'address_state', 'address_city',
                       'address_district', 'address_street', 'address_zip_code',
                       'address_number']
    
    def __str__(self):
        return self.email