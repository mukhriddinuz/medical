from django.urls import path
from .views import *

urlpatterns = [
    path('create-cassa/', CreateCassa.as_view()),
    path('get-cassa/', GetCassa.as_view()),

    path('create-employee/', CreateEmployee.as_view()),
    path('all-employee/', AllEmployee.as_view()),
    path('edit-employee/<int:pk>/', EditEmployee.as_view()),
    path('delete-employee/<int:pk>/', DeleteEmployee.as_view()),

    path('create-room/', CreateRoom.as_view()),
    path('all-room/', AllRoom.as_view()),
    path('edit-room/<int:pk>/', EditRoom.as_view()),
    path('delete-room/<int:pk>/', DeleteRoom.as_view()),

    path('create-equipment/', CreateEquipment.as_view()),
    path('all-equipment/', AllEquipment.as_view()),
    path('edit-equipment/<int:pk>/', EditEquipment.as_view()),
    path('delete-equipment/<int:pk>/', DeleteEquipment.as_view()),

    path('create-department/', CreateDepartment.as_view()),
    path('all-department/', AllDepartment.as_view()),
    path('edit-department/<int:pk>/', EditDepartment.as_view()),
    path('delete-department/<int:pk>/', DeleteDepartment.as_view()),

    path('create-doctor-specialty/', CreateDoctorSpecialty.as_view()),
    path('all-doctor-specialty/', AllDoctorSpecialty.as_view()),
    path('edit-doctor-specialty/<int:pk>/', EditDoctorSpecialty.as_view()),
    path('delete-doctor-specialty/<int:pk>/', DeleteDoctorSpecialty.as_view()),

    path('create-patient/', CreatePatient.as_view()),
    path('all-patient/', AllPatient.as_view()),
    path('edit-patient/<int:pk>/', EditPatient.as_view()),
    path('delete-patient/<int:pk>/', DeletePatient.as_view()),

    path('create-patient-illness/', CreatePatientIllness.as_view()),
    path('all-patient-illness/', AllPatientIllness.as_view()),
    path('edit-patient-illness/<int:pk>/', EditPatientIllness.as_view()),
    path('delete-patient-illness/<int:pk>/', DeletePatientIllness.as_view()),

    path('create-operation/', CreateOperation.as_view()),
    path('all-operation/', AllOperation.as_view()),
    path('edit-operation/<int:pk>/', EditOperation.as_view()),
    path('delete-operation/<int:pk>/', DeleteOperation.as_view()),

    path('create-feedback-patients/', CreateFeedbackPatients.as_view()),
    path('all-feedback-patients/', AllFeedbackPatients.as_view()),

    path('create-payment/', CreatePayment.as_view()),
    path('all-payment/', AllPayment.as_view()),

    path('create-attendance/', CreateAttendance.as_view()),
    path('all-attendance/', AllAttendance.as_view()),
    path('edit-attendance/<int:pk>/', EditAttendance.as_view()),
    path('delete-attendance/<int:pk>/', DeleteAttendance.as_view()),
]
