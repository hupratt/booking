from django.contrib import admin
from rooms.models import Room, RoomImage

# Register your models here.
class RoomModelAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price", "single_bed_number", "double_bed_number", "bath_number", "surface_area_sqmeter")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]
    # fieldsets = ((None, {"fields": [("name", "slug")]}),)
    class Meta:
        model = Room
admin.site.register(Room, RoomModelAdmin)



class RoomImageModelAdmin(admin.ModelAdmin):
    list_display = ['image','location','created']
    class Meta:
        model = RoomImage
admin.site.register(RoomImage, RoomImageModelAdmin)