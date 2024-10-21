from email.policy import default

from django.db import models
from django.contrib.auth.models import User


class PatientAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='patient_photos/', blank=True, null=True)
    medical_records_photo = models.ImageField(upload_to='medical_records/', blank=True, null=True)
    verification_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class DoctorAccount(models.Model):
    HOSPITAL_CHOICES = [
        ('Sacred Heart Medical Center', 'Sacred Heart Medical Center'),
        ('Angeles University Foundation Medical Center', 'Angeles University Foundation Medical Center'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    qualification = models.TextField(blank=True, null=True)
    years_of_experience = models.PositiveIntegerField()
    is_doctor = models.BooleanField(default=False)
    assigned_hospital = models.CharField(max_length=50, choices=HOSPITAL_CHOICES, default='Sacred Heart Medical Center')

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    patient = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='doctor_appointments', on_delete=models.CASCADE, null=True, blank=True)  # Add doctor field
    hospital = models.CharField(max_length=50, choices=[
        ('Sacred Heart Medical Center', 'Sacred Heart Medical Center'),
        ('Angeles University Foundation Medical Center', 'Angeles University Foundation Medical Center')
    ])
    appointment_date = models.DateTimeField()
    appointment_type = models.CharField(max_length=50, choices=[
        ('Check-up', 'Check-up'),
        ('Consultation', 'Consultation')
    ])
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.patient.username} - {self.appointment_type} with {self.hospital} on {self.appointment_date}"