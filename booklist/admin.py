from django.contrib import admin

# Register your models here.

from django.contrib import admin

from booklist.models import Book, Location, Category


class BookAdmin(admin.ModelAdmin):

    pass


class CategoryAdmin(admin.ModelAdmin):

    pass


class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)


