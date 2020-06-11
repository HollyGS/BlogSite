from django.contrib import admin
from .models import Post, Comment
from tinymce.widgets import TinyMCE
from django.db import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('body', 'name', 'email')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


# Register models
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
