from django.db import models
from base.models import ClassModel


class Category(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name of category')

    def __str__(self):
        return self.name

    def save(self):
        self.name = self.name.upper()
        super(Category, self).save()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']