
from django.contrib import admin

from nano.blog.models import *
from nano.blog.settings import NANO_BLOG_TAGS

tag_devel = None
untag_devel = None
if NANO_BLOG_TAGS:

    def tag_devel(modeladmin, request, queryset):
        for entry in queryset:
            entry.tags.add('devel')

    def untag_devel(modeladmin, request, queryset):
        for entry in queryset:
            entry.tags.remove('devel')

    tag_devel.short_description = "Tag selected entries with 'devel'"
    untag_devel.short_description = "Remove 'devel'-tag from selected entries"

class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ('headline', 'pub_date')
    search_fields = ('headline', 'pub_date')
    date_hierarchy = 'pub_date'
    if tag_devel and untag_devel:
        actions = [tag_devel, untag_devel]

admin.site.register(Entry, EntryAdmin)
