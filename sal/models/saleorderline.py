from django.db import models
from base.models import ClassModel
from django.utils import timezone
from .saleorder import SaleOrder
from inv.models.product import Product
from inv.models.uom import Uom
from acc.models.tax import Tax

STATE = (
        ('draft', 'Draft'),
        ('delivery', 'Delivery'),
        ('invoiced', 'Invoiced')
    )


class SaleOrderLine(ClassModel):
    sale_order_id = models.ForeignKey(
        SaleOrder,
        on_delete=models.PROTECT,
        verbose_name='Sale Order'
    )

    product_id = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name='Product'
    )

    description = models.TextField(blank=True, null=True)

    quantity = models.DecimalField(
        'Quantity',
        max_digits=10,
        decimal_places=2,
        default=0
    )

    invoiced_quantity = models.DecimalField(
        'Invoiced',
        max_digits=10,
        decimal_places=2,
        default=0
    )

    delivered_quantity = models.DecimalField(
        'Delivered',
        max_digits=10,
        decimal_places=2,
        default=0
    )

    uom_id = models.ForeignKey(
        Uom,
        verbose_name='UOM',
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )

    price = models.DecimalField(
        'Price',
        max_digits=10,
        decimal_places=2,
        default=0
    )

    tax_id = models.ManyToManyField(Tax, verbose_name='Tax', blank=True)

    amount_untaxed = models.DecimalField(
        'Amount un',
        max_digits=10,
        decimal_places=2,
        default=0
    )

    amount_tax_iva = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    amount_tax_other = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    amount_tax_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    amount_exempt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    amount_total = models.DecimalField(
        'Total',
        max_digits=10,
        decimal_places=2,
        default=0
    )

    class Meta:
        ordering = ['pk']
        verbose_name = 'Sale order line'
        verbose_name_plural = 'Sale orders line'