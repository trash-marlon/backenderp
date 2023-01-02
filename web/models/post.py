from django.db import models
from django.db.models import SET_NULL
from inv.models import Category
from base.models import ClassModel

class Post(ClassModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='web/post/images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['title']