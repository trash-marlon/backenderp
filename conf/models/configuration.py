from django.db import models
from base.models import ClassModel
from con.models.contact import Contact

class Configuration(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name of sale order')

    active_company_id = models.ForeignKey(
        Contact,
        on_delete=models.PROTECT,
        verbose_name=('Company'),
        null=True,
        blank=True
    )

    #www
    show_blog = models.BooleanField("Show Blog", default=False)
    show_shop = models.BooleanField("Show Shop", default=False)
    show_price = models.BooleanField("Show price", default=True)
    under_construction = models.BooleanField("Under Construction", default=False)
    user_register = models.BooleanField("User Register", default=False)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sale Order'
        verbose_name_plural = 'Sale Orders'
        ordering = ['name']