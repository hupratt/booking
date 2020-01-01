from schedule.views import (
    CalendarByPeriodsView
)
from rooms.models import RoomImage

class RoomView(CalendarByPeriodsView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        calendar = self.object
        room_images = RoomImage.objects.filter(location=calendar)
        context["room_images"] = room_images
        return context