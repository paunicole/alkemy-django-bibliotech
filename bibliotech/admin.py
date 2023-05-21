from django.contrib import admin
from .models.author import Author
from .models.employee import Employee
from .models.member import Member
from .models.book import Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [("first_name", "last_name"), "nationality", "is_active"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["is_active", "nationality"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [("first_name", "last_name"), "file_number", "is_active"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["is_active"]


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [("first_name", "last_name"), "birth_date", "is_active"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["is_active"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "isbn", "author", "is_active"]
    search_fields = ["title"]
    list_filter = ["is_active"]
