from django.db import models
from base.models import ClassModel

class Sequence(ClassModel):
    name = models.CharField(
        verbose_name="name",
        max_length=100,
        unique=True
    )

    prefix = models.CharField("Prefix", max_length=40, default='default')
    padding = models.PositiveIntegerField(
        verbose_name="padding",
        default=4
    )
    initial = models.PositiveIntegerField(
        verbose_name="initial",
        default=1
    )
    increment = models.PositiveIntegerField(
        verbose_name="increment",
        default=1
    )
    reset = models.PositiveIntegerField(
        verbose_name="reset",
        null=True,
        blank=True
    )
    last = models.PositiveIntegerField(verbose_name="Last", editable=False)
    next_val = models.PositiveIntegerField(verbose_name="Next")

    class Meta:
        verbose_name = "sequence"
        verbose_name_plural = "sequences"

    def __str__(self):
        return "name={}, prefix={}, last={}".format(
            repr(self.name), repr(self.prefix), repr(self.last))