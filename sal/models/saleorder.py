from django.db import models
from base.models import ClassModel
from con.models.contact import Contact


SALEORDER_STATE = (
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    )


class SaleOrder(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name of sale order')

    
    amount_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount_tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount_untaxed = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    partner_id = models.ForeignKey(
        Contact,
        on_delete=models.PROTECT,
        verbose_name=('Partner'),
        null=True,
        blank=True
    )

    state = models.CharField(
        choices=SALEORDER_STATE, max_length=64, default='draft')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sale Order'
        verbose_name_plural = 'Sale Orders'
        ordering = ['name']