from django.urls import path
from .views import *


urlpatterns = [
    path('user-fullname/', user_full_name),
    path('employee-by-position/', employee_by_position),
    path('employee-by-gender/', employee_by_gender),
    path('employee-by-address/', employee_by_address),
    path('employee-by-room_id/', employee_by_room_id),
    path('employee-by-salary/', employee_by_salary),
    path('department-by-patient/', department_by_patient),
    path('room-by-status/', room_by_status),
    path('room-by-capacity/', room_by_capacity),
    path('room-by-departament/', room_by_departament),
    path('room-by-is-blank/', room_by_is_blank),
    path('payment-by-summa/', payment_by_summa),
    path('payment-by-service/', payment_by_service),
    path('payment-by-datetime/', payment_by_datetime),
    path('payment-by-patient_id/', payment_by_patient_id),
    path('payment-by-category/', payment_by_category),
    path('patient-by-patient_illness/', patient_by_patient_illness),
    path('operation-by-start_time/', operation_by_start_time),
    path('operation-by-employee/', operation_by_employee),
    path('operation-by-room/', operation_by_room),
    path('department-by-name/', department_by_name),
    path('feedback-by-status/', feedback_by_status),
    path('equipment-by-name/', equipment_by_name),
    path('attendance-by-employee/', attendance_by_employee),
    path('attendance-by-date/', attendance_by_date),
]