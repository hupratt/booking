from django.db import models
from django.conf import settings
from django.urls import reverse
import os
from klingon.models import Translatable
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.forms import ValidationError
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from schedule.models import CalendarRelation, Calendar

class Location(models.Model, Translatable):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE,  help_text="(automatic) model linkage with the User")
    title = models.CharField(max_length=120, help_text="(required) title of the house/property card")
    gps_location = models.CharField(max_length=120, null=True, blank=True, help_text="(required) gps location of the house/property")
    gps_coordinates = models.CharField(max_length=120, null=True, blank=True, help_text="(required) gps coordinates of the house/property")
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, help_text="(automatic) timestamp for last update")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False, help_text="(automatic) timestamp for creation date")
    slug = models.SlugField(null=False, unique=True, help_text="(automatic) unique identifier for url location")
    tag = models.CharField(max_length=120, default="property", help_text="(automatic) unique tag")
    content = models.TextField(null=True, blank=True, help_text="(optional) description of the house/property")
    draft = models.BooleanField(default=False, help_text="(optional) description of the house/property")
    translatable_fields = ("title", "content")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})  


    class Meta:
        ordering = ["-timestamp", "-updated"]

    def get_like_url(self):
        return reverse(
            "like-toggle", kwargs={"slug": self.slug}
        )  # pylint: disable=no-member

    def get_api_like_url(self):
        return reverse(
            "like-api-toggle", kwargs={"slug": self.slug}
        )  # pylint: disable=no-member

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title[:49])  # pylint: disable=unsubscriptable-object

        super(Location, self).save(*args, **kwargs)

class LocationImage(models.Model):
    image = models.FileField( blank=True, null=True)
    location = models.ForeignKey("Location", on_delete=models.PROTECT, related_name='images')
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
