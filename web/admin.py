from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'published', 'fc', 'fm', 'uc', 'um']
    list_filter = ['published', 'category']
    search_fields = ['title', 'content']
    list_per_page = 10
    list_editable = ['published']
    # fieldsets = (
    #     ('Post', {
    #         'fields': (
    #             ('title', 'category'),
    #             'content',
    #             'image',
    #             'published',
    #         ),
    #     }),
    #     ('Metadata', {
    #         'fields': (
    #             ('fc', 'fm', 'uc', 'um'),
    #         ),
    #     }),
    # )
    # # readonly_fields = ('fc', 'fm', 'uc', 'um')
