from django.db import models
from base.models import ClassModel
from con.models.country import Country

POSITION_CHOICE = (
    ("before", "before to amount"),
    ('after', 'after to amount'),
)


class Currency(ClassModel):
    name = models.CharField('Name', max_length=40)
    alias = models.CharField('Alias', max_length=40)
    symbol = models.CharField('Symbol', max_length=15)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    iso = models.CharField(max_length=30)
    position = models.CharField(
        choices=POSITION_CHOICE, max_length=64, default='after')


    def __str__(self):
        return "{} ({})".format(self.name, self.country)

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

