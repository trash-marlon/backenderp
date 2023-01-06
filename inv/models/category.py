from django.db import models
from base.models import ClassModel


class Category(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name of category')

    for_website = models.BooleanField(default=False,
    help_text='Show on website')

    for_stock = models.BooleanField(default=True,
    help_text='Show on stock')

    parent_id = models.ForeignKey('self',  
    on_delete=models.PROTECT,
    verbose_name=('Parent'),
    null=True,
    blank=True,
    related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']