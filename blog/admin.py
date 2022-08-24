from django.contrib import admin
from . models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'update', 'is_published')
    list_display_links = ('id', 'title',)
    readonly_fields = ('date',)

admin.site.register(Blog, BlogAdmin)