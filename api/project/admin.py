from django.contrib import admin
from .models import Project, ProjectStatus, ProjectRole
from tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline


class TagInline(GenericTabularInline):
    model = TaggedItem
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines = (TagInline,)


class ProjectRoleAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProjectRole, ProjectRoleAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectStatus)

