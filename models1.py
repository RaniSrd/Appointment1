from django.db import models # type: ignore

class Appointment(models.Model):
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    person_name = models.CharField(max_length=255)
    person_dob = models.DateField()
    person_phone = models.CharField(max_length=15)
    person_email = models.EmailField()
    remarks = models.TextField(blank=True, null=True)
    meet_person_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Appointment with {self.meet_person_name} on {self.appointment_date}"
