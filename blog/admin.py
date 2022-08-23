from django.contrib import admin
from . models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    list_display_links = ('title',)

admin.site.register(Blog, BlogAdmin)