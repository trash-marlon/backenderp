from django.db import models
from django.contrib.auth.models import AbstractUser

SALE_PERMISSION = (
        ('none', 'none'),
        ('own', 'own'),
        ('all', 'all'),
        ('admin', 'admin'),
    )

PURCHASE_PERMISSION = (
        ('none', 'none'),
        ('own', 'own'),
        ('all', 'all'),
        ('admin', 'admin'),
    )



class User(AbstractUser):
    email = models.EmailField(unique=True)

    sale_permission = models.CharField(
        choices=SALE_PERMISSION, max_length=100, default='none')

    purchase_permission = models.CharField(
        choices=PURCHASE_PERMISSION, max_length=100, default='none')
        
    

    # If you whant to create a supersuper comment this line.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def full_name(self):
        return f'{self.first_name} {self.last_name}'