from django.contrib import admin

from blog.models import Post, Tag, TagPost


class TagInlineAdmin(admin.TabularInline):
    model = TagPost
    fk_name = 'post'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'updated_at']
    list_filter = ['title', 'created_at', 'updated_at', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [TagInlineAdmin]
    ordering = ['created_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    ordering = ['created_at']
