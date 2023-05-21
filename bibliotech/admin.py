from django.contrib import admin
from .models.author import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [("first_name", "last_name"), "nationality", "is_active"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["is_active", "nationality"]
