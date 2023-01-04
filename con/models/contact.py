from django.db import models
from django.db.models import SET_NULL
from base.models import ClassModel
from ..models.country import Country
from ..models.state import State

# Create your models here.

COMPANY_TYPE = (
        ('person', 'Person'),
        ('company', 'Company')
    )

class Contact(ClassModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    vat = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    street2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    own_company = models.BooleanField(default=False)
    zip = models.CharField(max_length=100, null=True, blank=True)
    
    country_id = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        verbose_name=('Country'),
        null=True,
        blank=True
    )

    state_id = models.ForeignKey(
        State,
        on_delete=models.PROTECT,
        verbose_name=('State'),
        null=True,
        blank=True
    )


    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    company_type = models.CharField(
        choices=COMPANY_TYPE, max_length=64, default='company')

    comment = models.TextField(null=True, blank=True)
    
    # Customer
    is_customer = models.BooleanField(default=False)
    customer_code = models.CharField(max_length=100, null=True, blank=True)

    # Supplier
    is_supplier = models.BooleanField(default=False)
    supplier_code = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact'
        verbose_name = 'Contact'