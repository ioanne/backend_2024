from django.contrib import admin

from book.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin with all fields """
    list_display = ["title"]
    search_fields = ["title"]
    list_per_page = 50
    fieldsets = (
        (None, {"fields": ("title",)}),
    )