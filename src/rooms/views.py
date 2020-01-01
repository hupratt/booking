from schedule.views import (
    CalendarByPeriodsView
)
from rooms.models import RoomImage, Room
from locations.models import Location
from schedule.models import CalendarRelation

class RoomView(CalendarByPeriodsView):
    model = Room
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        room = self.object
        context["room_images"] = room.get_room_images()
        context["parent_location"] = room.get_parent_location()
        return context