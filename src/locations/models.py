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
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=120)
    gps_location = models.CharField(max_length=120, null=True, blank=True)
    gps_coordinates = models.CharField(max_length=120, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(null=False, unique=True)
    tag = models.CharField(max_length=120, default="property")
    content = models.TextField(null=True, blank=True)
    draft = models.BooleanField(default=False)
    translatable_fields = ("title", "content")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "detail", kwargs={"slug": self.slug}
        )  # pylint: disable=no-member


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
