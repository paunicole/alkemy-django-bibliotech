from django.urls import path
from .views.books_api import *
from .views.members_api import *
from .views.employees_api import *
from .views.authors_api import *

urlpatterns = [
    path("books/", book_list, name="book-list-api"),
    path("books/<int:pk>/", book_id, name="book-id"),
    path("members/", member_list, name="member-list-api"),
    path("members/<int:pk>/", member_id, name="member-id"),
    path("employees/", employee_list, name="employee-list-api"),
    path("employees/<int:pk>/", employee_id, name="employee-id"),
    path("authors/", author_list, name="author-list-api"),
    path("authors/<int:pk>/", author_id, name="author-id"),
]
