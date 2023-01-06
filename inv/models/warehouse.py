from django.db import models
from base.models import ClassModel

class Warehouse(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name of Warehouse')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Warehouse'
        verbose_name_plural = 'Warehouses'
        ordering = ['name']