from django.db import models
from schedule.models import Calendar
import os
from locations.models import Location
from schedule.models import CalendarRelation
from django.urls import reverse
# Create your models here.

class Room(Calendar):

    price = models.PositiveSmallIntegerField(help_text="(required) price per night per person")
    single_bed_number = models.PositiveSmallIntegerField(help_text="(required) number of single beds in the room")
    double_bed_number = models.PositiveSmallIntegerField(help_text="(required) number of double beds in the room")
    bath_number = models.PositiveSmallIntegerField(help_text="(required) number of bathrooms in the room")
    surface_area_sqmeter = models.PositiveSmallIntegerField(help_text="(required) surface of the room in square meters")
    description = models.CharField(max_length=120, null=True, blank=True, help_text="(optional) room description")

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
    image = models.FileField( blank=True, null=True, help_text="(optional) room image field")
    location = models.ForeignKey("Room", on_delete=models.PROTECT, related_name='room_image', help_text="(automatic) room model linkage")
    created = models.DateTimeField(auto_now_add=True, help_text="(automatic) created date")
    alt = models.CharField(max_length=120, default="blank", help_text="(required) SEO for images in order to provide accessibility for the visually impaired")

    def __str__(self):
        return self.alt
            
    def __unicode__(self):
        return self.alt



