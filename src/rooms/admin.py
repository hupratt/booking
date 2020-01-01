from django.contrib import admin
from rooms.models import Room

# Register your models here.
class RoomModelAdmin(admin.ModelAdmin):
    # list_display = ("name", "slug", "price", "single_bed_number", "double_bed_number")
    prepopulated_fields = {"slug": ("name",)}
    # search_fields = ["name"]
    # fieldsets = ((None, {"fields": [("name", "slug")]}),)
    class Meta:
        model = Room
admin.site.register(Room, RoomModelAdmin)