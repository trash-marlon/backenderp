from django.db import models
from base.models import ClassModel
from con.models.country import Country

STATE = (
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    )

TYPE = (
        ('sale', 'Sale'),
        ('purchase', 'Purchase'),
    )

class Tax(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name of sale order')

    state = models.CharField(
        choices=STATE, max_length=64, default='draft')

    typeTax = models.CharField(
        choices=TYPE, max_length=64, default='sale')

    include_price = models.BooleanField("Include Price", default=True, blank=True, null=True)


    country_id = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        verbose_name=('Country'),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxes'
        ordering = ['name']