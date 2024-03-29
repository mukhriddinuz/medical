from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import *


@admin.register(User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('phone_number', "slug",)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Cassa)
admin.site.register(Employee)
admin.site.register(Room)
admin.site.register(Equipment)
admin.site.register(Department)
admin.site.register(DoctorSpecialty)
admin.site.register(Patient)
admin.site.register(PatientIllness)
admin.site.register(Operation)
admin.site.register(FeedbackPatients)
admin.site.register(Payment)
admin.site.register(Attendance)

