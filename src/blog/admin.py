from django.contrib import admin

from .models import (
    Post,
    Tag,
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

    list_display_links = ('title', )

    prepopulated_fields = {'slug': ('title', )}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    list_display_links = ('name', )

    prepopulated_fields = {'slug': ('name', )}

