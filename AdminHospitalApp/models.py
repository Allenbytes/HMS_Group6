from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    index_number = models.PositiveIntegerField(unique=True)  # Adding index number
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='inventory_images/', blank=True, null=True)  # Adding image field

    def __str__(self):
        return f"{self.index_number} - {self.name}"


from django.db import models

class FinancialRecord(models.Model):
    TRANSACTION_TYPES = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Approvement(models.Model):
    patient = models.ForeignKey(User, related_name='approved_appointments', on_delete=models.CASCADE)
    hospital = models.CharField(max_length=50, choices=[
        ('Sacred Heart Medical Center', 'Sacred Heart Medical Center'),
        ('Angeles University Foundation Medical Center', 'Angeles University Foundation Medical Center')
    ])
    appointment_date = models.DateTimeField()
    appointment_type = models.CharField(max_length=50, choices=[
        ('Check-up', 'Check-up'),
        ('Consultation', 'Consultation')
    ])
    status = models.CharField(max_length=20, default='Approved')
    doctor = models.ForeignKey(User, related_name='assigned_appointments', on_delete=models.CASCADE)  # New field for assigned doctor

    def __str__(self):
        return f"{self.patient.username} - {self.appointment_type} with {self.hospital} on {self.appointment_date}"