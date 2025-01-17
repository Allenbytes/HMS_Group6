# Generated by Django 5.1.1 on 2024-10-21 03:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminHospitalApp', '0002_auto_20241018_0939'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='financialrecord',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Approvement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.CharField(choices=[('Sacred Heart Medical Center', 'Sacred Heart Medical Center'), ('Angeles University Foundation Medical Center', 'Angeles University Foundation Medical Center')], max_length=50)),
                ('appointment_date', models.DateTimeField()),
                ('appointment_type', models.CharField(choices=[('Check-up', 'Check-up'), ('Consultation', 'Consultation')], max_length=50)),
                ('status', models.CharField(default='Approved', max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_appointments', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approved_appointments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
