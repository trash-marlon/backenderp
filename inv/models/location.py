from django.db import models
from base.models import ClassModel
from inv.models.warehouse import Warehouse


class Location(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name of location')

    warehouse_id = models.ForeignKey(
        Warehouse,
        related_name='location',
        on_delete=models.PROTECT,
        verbose_name='Warehouse',
        null=True,
        blank=True
    )

    parent_id = models.ForeignKey('self',  
    on_delete=models.PROTECT,
    verbose_name=('Parent'),
    null=True,
    blank=True,
    related_name='children')

    code = models.CharField(max_length=3,
    unique=True,
    help_text='Code')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        ordering = ['name']