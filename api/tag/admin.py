from django.contrib import admin
from .models import TagType, TagCategory, Tag

admin.site.register(TagType)
admin.site.register(TagCategory)
admin.site.register(Tag)

