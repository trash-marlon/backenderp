from django.db import models
from base.models import ClassModel


class Brand(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name of Brand')

    parent_id = models.ForeignKey('self',  
    on_delete=models.PROTECT,
    verbose_name=('Parent'),
    null=True,
    blank=True,
    related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['name']