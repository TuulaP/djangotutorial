from django.contrib import admin

# Register your models here.

from django.contrib import admin

from projects.models import Project


class PostAdmin(admin.ModelAdmin):

    pass


admin.site.register(Project)