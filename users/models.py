from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    # If you whant to create a supersuper comment this line.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []