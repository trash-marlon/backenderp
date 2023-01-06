from django.db import models
from base.models import ClassModel
from con.models.contact import Contact
from django.utils import timezone

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
        related_name='sale_order_partner',
        on_delete=models.PROTECT,
        verbose_name='Partner',
        null=True,
        blank=True
    )

    seller_id = models.ForeignKey(
        Contact,
        on_delete=models.PROTECT,
        related_name='sale_order_seller',
        verbose_name='Seller',
        null=True,
        blank=True
    )

    state = models.CharField(
        choices=SALEORDER_STATE, max_length=64, default='draft')

    date_order = models.DateTimeField(default=timezone.now, null=True, blank=True)
    date_confirm = models.DateTimeField(null=True)
    note = models.TextField('Note', blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sale Order'
        verbose_name_plural = 'Sale Orders'
        ordering = ['pk']

    
    def save(self, *args, **kwargs):
        # if not self.pk:
        #     self.name = get_next_value(self._meta.object_name, 'SO')

        if not self.date_order or self.date_order == "":
            self.date_order = default=timezone.now
        super().save(*args, **kwargs)