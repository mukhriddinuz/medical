from django.urls import path
from .views import *


urlpatterns = [
    path('user-fullname/', user_full_name),
    path('employee-by-position/', employee_by_position),
    path('employee-by-gender/', employee_by_gender),
    path('employee-by-address/', employee_by_address),
    path('employee-by-room_id/', employee_by_room_id),
    path('employee-by-salary/', employee_by_salary),
    path('department_by_patient/', department_by_patient),
    path('room_by_status/', room_by_status),
    path('room_by_capacity/', room_by_capacity),
    path('room_by_departament/', room_by_departament),
    path('room_by_is_blank/', room_by_is_blank),
    path('payment_by_summa/', payment_by_summa),
    path('payment_by_service/', payment_by_service),
    path('payment_by_datetime/', payment_by_datetime),
    path('payment_by_patient_id/', payment_by_patient_id),
    path('payment_by_category/', payment_by_category),
]