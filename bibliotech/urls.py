from django.urls import path
from .views import employee_views


urlpatterns = [
    path("employee/new", employee_views.employee_form, name="employee-form"),
    path("employee-list", employee_views.employee_list, name="employee-list"),
]
