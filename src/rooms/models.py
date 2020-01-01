from django.db import models
from schedule.models import Calendar

# Create your models here.

class Room(Calendar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
    price = models.PositiveSmallIntegerField()
    single_bed_number = models.PositiveSmallIntegerField()
    double_bed_number = models.PositiveSmallIntegerField()
    bath_number = models.PositiveSmallIntegerField()
    surface_area_sqmeter = models.PositiveSmallIntegerField()