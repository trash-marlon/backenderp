from django.db import models
from base.models import ClassModel


class Uom(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name of Uom')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Uom'
        verbose_name_plural = 'Uoms'
        ordering = ['name']