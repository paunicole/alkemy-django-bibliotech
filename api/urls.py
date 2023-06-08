from django.urls import path, include
from rest_framework import routers
from .views import author_view, book_view, employee_view, member_view

router = routers.DefaultRouter()

router.register(r"authors", author_view.AuthorViewSet, "author-api")
router.register(r"books", book_view.BookViewSet, "book-api")
router.register(r"employees", employee_view.EmployeeViewSet, "employee-api")
router.register(r"members", member_view.MemberViewSet, "member-api")

urlpatterns = [path("", include(router.urls))]
