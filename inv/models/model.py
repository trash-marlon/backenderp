from django.db import models
from base.models import ClassModel
from inv.models.brand import Brand


class Model(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name of the model')

    brand_id = models.ForeignKey(
        Brand,
        related_name='brand',
        on_delete=models.PROTECT,
        verbose_name='Brand',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'
        ordering = ['name']