from django.contrib import admin

from blog.models import Post, Tag, TagPost


class TagInlineAdmin(admin.TabularInline):
    model = TagPost
    fk_name = 'post'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title', 'tags']
    inlines = [TagInlineAdmin]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
