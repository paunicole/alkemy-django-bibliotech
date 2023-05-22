from django.contrib import admin
from .models.author import Author
from .models.employee import Employee
from .models.member import Member
from .models.book import Book
from .models.lendbook import LendBook


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = [("first_name", "last_name"), "nationality", "is_active"]
    list_display = ["first_name", "last_name", "nationality", "is_active"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["is_active", "nationality"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = [("first_name", "last_name"), "file_number", "is_active"]
    list_display = ["first_name", "last_name", "file_number", "is_active"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["is_active"]


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    fields = [("first_name", "last_name"), "birth_date", "is_active"]
    list_display = ["first_name", "last_name", "birth_date", "is_active"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["is_active"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "isbn", "author", "is_active"]
    search_fields = ["title"]
    list_filter = ["is_active"]


@admin.register(LendBook)
class LendBookAdmin(admin.ModelAdmin):
    list_display = ["lend_date", "return_date", "member", "book", "employee"]
    search_fields = ["member", "book", "employee"]
