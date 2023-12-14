
# appointments/models.py
from django.db import models

class Appointment(models.Model):
    patient_name = models.CharField(max_length=255)
    doctor = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    mobile_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.patient_name} - {self.date} {self.time}"
 