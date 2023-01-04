from django.db import models
from base.models import ClassModel


class Product(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name of Product')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']