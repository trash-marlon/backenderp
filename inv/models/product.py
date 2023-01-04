from django.db import models
from base.models import ClassModel
from inv.models.category import Category

PRODUCT_TYPE = (
        ('service', 'Service'),
        ('product', 'Product'),
        ('cons', 'Consumable'),
    )


class Product(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name of Product')

    type = models.CharField(
        choices=PRODUCT_TYPE, max_length=100, default='product')

    category_id = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name=('Category'),
        null=True,
        blank=True
    )
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    for_sale = models.BooleanField(default=True)
    for_purchase = models.BooleanField(default=True)

    code = models.CharField(max_length=100,
    unique=True,
    null=True,
    blank=True,
    help_text='Code of Product')

    barcode = models.CharField(max_length=100,
    unique=True,
    null=True,
    blank=True,
    help_text='Barcode of Product')

    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        help_text='Description of Product')
    