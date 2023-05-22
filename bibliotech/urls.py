from django.urls import path
from .views import employee_views


urlpatterns = [
    path("employee/new", employee_views.employee_form, name="employee_form"),
    path("employee_list", employee_views.employee_list, name="employee_list"),
]
