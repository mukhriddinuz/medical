from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView
from .models import *
from .serializers import *


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
    patient = PatientIllness.objects.filter(department=department)
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
    blank = request.GET.get('blank')
    room = Room.objects.filter(blank=blank)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)









