from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
import qrcode
from io import BytesIO
from django.core.files import File
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import re


class Cassa(models.Model):
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.total_amount}"


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex=r'^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number'
        )
    ])
    slug = models.SlugField(max_length=255, null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        self.slug = self.first_name + "_" + self.last_name
        super().save(*args, **kwargs)


class Employee(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    POSITION_CHOICES = (
        (0, 'Doctor'),
        (1, 'Manager'),
        (2, 'Reception'),
        (3, "Master")
    )
    position = models.IntegerField(default=0, choices=POSITION_CHOICES)
    GENDER = (
        (0, "Male"),
        (1, "Famale")
    )
    gender = models.IntegerField(default=0, choices=GENDER)
    birthday = models.DateField()
    address = models.CharField(max_length=255)
    room = models.ForeignKey(to='Room', on_delete=models.PROTECT)
    salary = models.IntegerField(default=0)
    specialty_id = models.ForeignKey(to='DoctorSpecialty', on_delete=models.PROTECT)
    department = models.ForeignKey(to="Department", on_delete=models.PROTECT)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.first_name}"


class Room(models.Model):
    name = models.CharField(max_length=150)
    capacity = models.IntegerField()
    STATUS = (
        (0, "LUX"),
        (1, "ECONOM"),
        (2, "Other")
    )
    status = models.IntegerField(default=0, choices=STATUS)
    department = models.ForeignKey(to='Department', on_delete=models.PROTECT)
    equipment = models.ManyToManyField(to="Equipment", blank=True)
    other_info = models.TextField()
    number_of_blank = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.number_of_blank is None:
            self.number_of_blank = self.capacity
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.capacity}"


class Equipment(models.Model):
    name = models.CharField(max_length=150)
    number = models.IntegerField(default=1)
    extra_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DoctorSpecialty(models.Model):
    specialty_name = models.CharField(max_length=150)

    def __str__(self):
        return self.specialty_name


class Patient(models.Model):
    full_name = models.CharField(max_length=255)
    birthday = models.DateField()
    address = models.CharField(max_length=255)
    passport_number = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


class PatientIllness(models.Model):
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)
    illness_name = models.CharField(max_length=255)
    department = models.ForeignKey(to=Department, on_delete=models.PROTECT)
    treatment_started = models.DateTimeField()
    treatment_ended = models.DateTimeField(null=True, blank=True)
    doctor = models.ForeignKey(to=Employee, on_delete=models.DO_NOTHING)
    room = models.ForeignKey(to=Room, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.patient.full_name} - {self.illness_name}"


class Operation(models.Model):
    room = models.ForeignKey(to=Room, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)
    employee = models.ManyToManyField(to=Employee)
    info = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.patient.full_name} - {self.room.name}"


class FeedbackPatients(models.Model):
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)
    TYPE = (
        (0, "suggestions"),
        (1, "complaints"),
        (2, "comments"),
    )
    type = models.IntegerField(default=2, choices=TYPE)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient.full_name


class Payment(models.Model):
    payment_amount = models.DecimalField(max_digits=20, decimal_places=2)
    SERVICE = (
        (0, "for treatment"),
        (1, "for the operation"),
        (2, "for equipment"),
        (3, "other")
    )
    service = models.IntegerField(default=0, choices=SERVICE)
    info = models.CharField(max_length=255)
    is_payment = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE, null=True, blank=True)
    CATEGORY = (
        (0, 'Income'),
        (1, 'Expenses')
    )
    category = models.IntegerField(default=0, choices=CATEGORY)
    qr_code = models.ImageField(upload_to='qr_code_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.payment_amount}\n{self.service}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.datetime}.png', File(buffer), save=False)

        super().save(*args, **kwargs)


class Attendance(models.Model):
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = ["employee", "date"]

    def clean(self):
        if self.check_out and self.check_out < self.check_in:
            raise ValidationError("Check-out time must be after check-in time.")

    def __str__(self):
        return f"{self.employee.user.first_name} - {self.date}"

