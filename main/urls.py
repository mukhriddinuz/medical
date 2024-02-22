from django.urls import path
from .views import *


urlpatterns = [
    path('employee-by-position/', employee_by_position)
]