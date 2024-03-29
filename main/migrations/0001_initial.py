# Generated by Django 5.0.2 on 2024-02-20 16:42

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cassa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('number', models.IntegerField(default=1)),
                ('extra_info', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('passport_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Invalid phone number', regex='^[\\+]9{2}8{1}[0-9]{9}$')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(choices=[(0, 'Doctor'), (1, 'Manager'), (2, 'Reception'), (3, 'Master')], default=0)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Famale')], default=0)),
                ('birthday', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('salary', models.IntegerField(default=0)),
                ('bio', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.department')),
                ('specialty_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.doctor_specialty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackPatients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'suggestions'), (1, 'complaints'), (2, 'comments')], default=2)),
                ('text', models.TextField()),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('service', models.IntegerField(choices=[(0, 'for treatment'), (1, 'for the operation'), (2, 'for equipment'), (3, 'other')], default=0)),
                ('info', models.CharField(max_length=255)),
                ('is_payment', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('category', models.IntegerField(choices=[(0, 'Income'), (1, 'Expenses')], default=0)),
                ('qr_code', models.ImageField(upload_to='qr_code_images/')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('capacity', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'LUX'), (1, 'ECONOM'), (2, 'Other')], default=0)),
                ('other_info', models.TextField()),
                ('number_of_blank', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.department')),
                ('equipment', models.ManyToManyField(to='main.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='PatientIllness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('illness_name', models.CharField(max_length=255)),
                ('treatment_started', models.DateTimeField()),
                ('treatment_ended', models.DateTimeField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.department')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.employee')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.room')),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('employee', models.ManyToManyField(to='main.employee')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.room')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.room'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('check_in', models.TimeField(blank=True, null=True)),
                ('check_out', models.TimeField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
            ],
            options={
                'unique_together': {('employee', 'date')},
            },
        ),
    ]
