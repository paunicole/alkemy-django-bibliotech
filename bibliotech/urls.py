from django.urls import path
from .views import employee_views
from .views import author_views
from .views import member_views
from .views import book_views

urlpatterns = [
    path("employee/new", employee_views.employee_create, name="employee-create"),
    path("employee-list", employee_views.employee_list, name="employee-list"),
    path(
        "employee/update/<str:employee_id>",
        employee_views.employee_update,
        name="employee-update",
    ),
    path(
        "employee/disable/<str:pk>",
        employee_views.employee_disable,
        name="employee-disable",
    ),
    path(
        "employee/enable/<str:pk>",
        employee_views.employee_enable,
        name="employee-enable",
    ),
    path("author/new", author_views.author_create, name="author-create"),
    path("author-list", author_views.author_list, name="author-list"),
    path(
        "author/update/<str:author_id>",
        author_views.author_update,
        name="author-update",
    ),
    path(
        "author/disable/<str:pk>",
        author_views.author_disable,
        name="author-disable",
    ),
    path(
        "author/enable/<str:pk>",
        author_views.author_enable,
        name="author-enable",
    ),
    path("member/new", member_views.member_create, name="member-create"),
    path("member-list", member_views.member_list, name="member-list"),
    path(
        "member/update/<str:member_id>",
        member_views.member_update,
        name="member-update",
    ),
    path(
        "member/disable/<str:pk>",
        member_views.member_disable,
        name="member-disable",
    ),
    path(
        "member/enable/<str:pk>",
        member_views.member_enable,
        name="member-enable",
    ),
    path("book/new", book_views.book_create, name="book-create"),
    path(
        "book/update/<str:book_id>",
        book_views.book_update,
        name="book-update",
    ),
    path(
        "book/disable/<str:pk>",
        book_views.book_disable,
        name="book-disable",
    ),
    path(
        "book/enable/<str:pk>",
        book_views.book_enable,
        name="book-enable",
    ),
]
