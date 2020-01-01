from schedule.views import (
    CalendarByPeriodsView
)
from rooms.models import RoomImage, Room
from locations.models import Location
from schedule.models import CalendarRelation
from django.conf import settings
from django.views.generic.list import ListView
class RoomView(CalendarByPeriodsView):
    # override the "tri_month_calendar" from the "schedule" app
    model = Room
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        room = self.object
        context["room_images"] = room.get_room_images()
        context["parent_location"] = room.get_parent_location()
        context["phone_number"] = settings.COMMERCIAL_PHONE_NUMBER
        return context

class RoomsListView(ListView):
    model = Room
    paginate_by = 10 
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context