from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView
from main.models import *
from main.serializers import *


""" START CRUD CASSA """


class CreateCassa(ListCreateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializer


class GetCassa(ListAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializer


"""END CRUD CASSA"""

"""START CRUD EMPLOYEE"""


class CreateEmployee(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AllEmployee(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EditEmployee(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeleteEmployee(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


"""END CRUD EMPLOYEE"""

"""START CRUD ROOM"""


class CreateRoom(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class AllRoom(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class EditRoom(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class DeleteRoom(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


"""END CRUD ROOM"""

"""START CRUD EQUIPMENT"""


class CreateEquipment(ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class AllEquipment(ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EditEquipment(UpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class DeleteEquipment(DestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


"""END CRUD EQUIPMENT"""

"""START CRUD DEPARTMENT"""


class CreateDepartment(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class AllDepartment(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EditDepartment(UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DeleteDepartment(DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


"""END CRUD DEPARTMENT"""

"""START CRUD DoctorSpecialty"""


class CreateDoctorSpecialty(ListCreateAPIView):
    queryset = DoctorSpecialty.objects.all()
    serializer_class = DoctorSpecialtySerializer


class AllDoctorSpecialty(ListAPIView):
    queryset = DoctorSpecialty.objects.all()
    serializer_class = DoctorSpecialtySerializer


class EditDoctorSpecialty(UpdateAPIView):
    queryset = DoctorSpecialty.objects.all()
    serializer_class = DoctorSpecialtySerializer


class DeleteDoctorSpecialty(DestroyAPIView):
    queryset = DoctorSpecialty.objects.all()
    serializer_class = DoctorSpecialtySerializer


"""END CRUD DoctorSpecialty"""

"""START CRUD PATIENT"""


class CreatePatient(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AllPatient(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class EditPatient(UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DeletePatient(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


"""END CRUD PATIENT"""

"""START CRUD PatientIllness"""


class CreatePatientIllness(ListCreateAPIView):
    queryset = PatientIllness.objects.all()
    serializer_class = PatientIllnessSerializer


class AllPatientIllness(ListAPIView):
    queryset = PatientIllness.objects.all()
    serializer_class = PatientIllnessSerializer


class EditPatientIllness(UpdateAPIView):
    queryset = PatientIllness.objects.all()
    serializer_class = PatientIllnessSerializer


class DeletePatientIllness(DestroyAPIView):
    queryset = PatientIllness.objects.all()
    serializer_class = PatientIllnessSerializer


"""END CRUD PatientIllness"""

"""START CRUD OPERATION"""


class CreateOperation(ListCreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class AllOperation(ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class EditOperation(UpdateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class DeleteOperation(DestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


"""END CRUD OPERATION"""

"""START CRUD FeedbackPatients"""


class CreateFeedbackPatients(ListCreateAPIView):
    queryset = FeedbackPatients.objects.all()
    serializer_class = FeedbackPatientsSerializer


class AllFeedbackPatients(ListAPIView):
    queryset = FeedbackPatients.objects.all()
    serializer_class = FeedbackPatientsSerializer


"""END CRUD FeedbackPatients"""

"""START CRUD PAYMENT"""


class CreatePayment(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class AllPayment(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


"""END CRUD PAYMENT"""

"""START CRUD ATTENDANCE"""


class CreateAttendance(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AllAttendance(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class EditAttendance(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class DeleteAttendance(DestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


"""END CRUD ATTENDANCE"""