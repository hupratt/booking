from django.db import models
from schedule.models import Calendar
import os
from locations.models import Location
from schedule.models import CalendarRelation
from django.urls import reverse
# Create your models here.

class Room(Calendar):

    price = models.PositiveSmallIntegerField()
    single_bed_number = models.PositiveSmallIntegerField()
    double_bed_number = models.PositiveSmallIntegerField()
    bath_number = models.PositiveSmallIntegerField()
    surface_area_sqmeter = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=120, null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("tri_month_calendar", kwargs={"calendar_slug": self.slug})
        
    def max_capacity(self):
        return self.single_bed_number + self.double_bed_number *2

    def get_parent_location(self):
        calendarRelation_qs = CalendarRelation.objects.filter(calendar_id=self.id)
        if len(calendarRelation_qs)>1:
            return None
        parent_location_id = calendarRelation_qs[0].object_id
        parent_location = Location.objects.filter(id=parent_location_id)
        if len(parent_location)>1:
            raise ValueError("A room can only have one parent location")
        return parent_location[0]

    def get_room_thumbnail(self):
        return self.get_room_images()[0]

    def get_room_images(self):
        return RoomImage.objects.filter(location_id=self.id)

class RoomImage(models.Model):
    image = models.FileField( blank=True, null=True)
    location = models.ForeignKey("Room", on_delete=models.PROTECT, related_name='room_image')
    created = models.DateTimeField(auto_now_add=True)
    alt = models.CharField(max_length=120, default="blank")

    def __str__(self):
        return self.alt
            
    def __unicode__(self):
        return self.alt



