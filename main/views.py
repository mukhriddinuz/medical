from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView
from .models import *
from .serializers import *
from datetime import datetime


@api_view(["GET"])
def user_full_name(request):
    full_name = request.GET.get('full_name')
    user = User.objects.filter(slug__icontains=full_name)
    ser = UserSerializer(user, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_position(request):
    position = request.GET.get('position')
    employee = Employee.objects.filter(position=position)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_gender(request):
    gender = request.GET.get('gender')
    employee = Employee.objects.filter(gender=gender)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_address(request):
    address = request.GET.get('address')
    employee = Employee.objects.filter(address=address)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_room_id(request):
    room_id = request.GET.get('room_id')
    employee = Employee.objects.filter(room_id=room_id)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_salary(request):
    salary = request.GET.get('salary')
    employee = Employee.objects.filter(salary=salary)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_speciality_id(request):
    speciality_id = request.GET.get('speciality_id')
    employee = Employee.objects.filter(speciality_id=speciality_id)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def department_by_patient(request):
    department = request.GET.get('department')
    patient = PatientIllness.objects.filter(department=department, treatment_ended=None)
    ser = PatientIllnessSerializer(patient, many=True)
    return Response(ser.data)


@api_view(["GET"])
def room_by_status(request):
    status = request.GET.get('status')
    room = Room.objects.filter(status=status)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(["GET"])
def room_by_capacity(request):
    capacity = request.GET.get('capacity')
    room = Room.objects.filter(capacity=capacity)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(["GET"])
def room_by_departament(request):
    departament = request.GET.get('departament')
    room = Room.objects.filter(departament=departament)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(["GET"])
def room_by_is_blank(request):
    capacity = request.GET.get('capacity')
    status = request.GET.get('status')
    department = request.GET.get('department')
    room = Room.objects.filter(capacity=capacity, status=status, department_id=department, number_of_blank__gt=0)
    ser = RoomSerializer(room, many=True).data
    return Response(ser)


@api_view(["GET"])
def payment_by_summa(request):
    summa = request.GET.get('summa')
    payment = Payment.objects.filter(summa=summa)
    ser = PaymentSerializer(payment, many=True)
    return Response(ser.data)


@api_view(["GET"])
def payment_by_service(request):
    service = request.GET.get('service')
    payment = Payment.objects.filter(service=service)
    ser = PaymentSerializer(payment, many=True)
    return Response(ser.data)


@api_view(["GET"])
def payment_by_datetime(request):
    datetime = request.GET.get('datetime')
    payment = Payment.objects.filter(datetime=datetime)
    ser = PaymentSerializer(payment, many=True)
    return Response(ser.data)


@api_view(["GET"])
def payment_by_patient_id(request):
    patient_id = request.GET.get('patient_id')
    payment = Payment.objects.filter(patient_id=patient_id)
    ser = PaymentSerializer(payment, many=True)
    return Response(ser.data)


@api_view(["GET"])
def payment_by_category(request):
    category = request.GET.get('category')
    payment = Payment.objects.filter(category=category)
    ser = PaymentSerializer(payment, many=True)
    return Response(ser.data)


@api_view(['GET'])
def patient_by_patient_illness(request):
    patient = request.GET.get('patient')
    patient_illness = PatientIllness.objects.filter(patient_id=patient).order_by('-id')
    ser = PatientSerializer(patient_illness, many=True)
    return Response(ser.data)


@api_view(['GET'])
def operation_by_start_time(request):
    start_date_str = request.GET.get('start_date')
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
    operations = Operation.objects.filter(start_time__date=start_date)
    ser = OperationSerializer(operations, many=True)
    return Response(ser.data)


@api_view(['GET'])
def operation_by_employee(request):
    employees = request.GET.getlist('employees')
    operation = Operation.objects.filter(id__in=employees)
    ser = OperationSerializer(operation, many=True)
    return Response(ser.data)


@api_view(['GET'])
def operation_by_room(request):
    room = request.GET.get('room')
    current_time = datetime.now()
    operation = Operation.objects.filter(room_id=room, start_time__gte=current_time)
    ser = OperationSerializer(operation, many=True)
    return Response(ser.data)


@api_view(['GET'])
def department_by_name(request):
    department_name = request.GET.get('department_name')
    department = Department.objects.filter(name__icontains=department_name)
    ser = DepartmentSerializer(department, many=True)
    return Response(ser.data)


@api_view(['GET'])
def equipment_by_name(request):
    equipment_name = request.GET.get('equipment_name')
    equipment = Equipment.objects.filter(name__icontains=equipment_name)
    ser = EquipmentSerializer(equipment, many=True)
    return Response(ser.data)


@api_view(['GET'])
def feedback_by_status(request):
    status = request.GET.get('status')
    feedback = FeedbackPatients.objects.filter(status=status).order_by('-id')
    ser = FeedbackPatientsSerializer(feedback, many=True)
    return Response(ser.data)


@api_view(['GET'])
def attendance_by_employee(request):
    employee = request.GET.get('employee')
    attendance = Attendance.objects.filter(employee_id=employee).order_by('-id')
    ser = AttendanceSerializer(attendance, many=True)
    return Response(ser.data)


@api_view(['GET'])
def attendance_by_date(request):
    date = request.GET.get('date')
    print(date)
    attendance = Attendance.objects.filter(date=date).order_by('-id')
    ser = AttendanceSerializer(attendance, many=True)
    return Response(ser.data)
