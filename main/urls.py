from django.urls import path
from .views import *


urlpatterns = [
    path('employee-by-position/', employee_by_position),
    path('employee-by-gender/', employee_by_gender),
    path('employee-by-address/', employee_by_address),
    path('employee-by-room_id/', employee_by_room_id),
    path('employee-by-salary/', employee_by_salary),
    path('department_by_patient/', department_by_patient),
]