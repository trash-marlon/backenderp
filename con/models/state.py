from django.db import models
from base.models import ClassModel
# from ..models.country import Country

class State(ClassModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    # country_id = models.ForeignKey(
    #     Country,
    #     on_delete=models.PROTECT,
    #     verbose_name=('Country'),
    #     null=True,
    #     blank=True
    # )

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'
        ordering = ['name']