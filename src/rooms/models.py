from django.db import models
from schedule.models import Calendar
import os

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

class RoomImage(models.Model):
    image = models.FileField( blank=True, null=True)
    location = models.ForeignKey("Room", on_delete=models.PROTECT, related_name='room_image')
    created = models.DateTimeField(auto_now_add=True)
    alt = models.CharField(max_length=120, default="blank")

    def __str__(self):
        return self.alt
            
    def __unicode__(self):
        return self.alt

    @staticmethod
    def get_image_path(instance):
        return os.path.join(
            "static", instance.id
        )  
