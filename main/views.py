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

