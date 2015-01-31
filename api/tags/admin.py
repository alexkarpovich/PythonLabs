from django.contrib import admin
from .models import TagCategory, Tag


class TagCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)
admin.site.register(TagCategory, TagCategoryAdmin)