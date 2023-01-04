from django.db import models
from django.contrib.auth.models import AbstractUser

SALE_PERMISSION = (
        ('own', 'own'),
        ('all', 'all'),
        ('admin', 'admin'),
    )

class User(AbstractUser):
    email = models.EmailField(unique=True)

    sale_permission = models.CharField(
        choices=SALE_PERMISSION, max_length=100, default='admin')
    

    # If you whant to create a supersuper comment this line.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []