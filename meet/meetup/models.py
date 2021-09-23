from enum import auto
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Meetslot(models.Model):
    slot_booked_by = models.CharField(max_length=100, default='')
    slot_time = models.TimeField()
    slot_date = models.DateField()
    slot_booked = models.CharField(max_length=15, default='Not Booked')

    def __str__(self):
        return self.slot_date