# from django.conf import settings
# from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path 
from django.conf.urls import url, include
from django.views.generic.list import ListView

# from schedule.feeds import CalendarICalendar, UpcomingEventsFeed
# from schedule.models import Calendar
from schedule.periods import Day, Month, Week, Year
from schedule.views import (
    CalendarByPeriodsView
)
from .views import RoomView, RoomsListView


urlpatterns = [
    path('list/', RoomsListView.as_view(template_name="list.html"), name='rooms-list'), 
    path('schedule/', include('schedule.urls')),
    path('schedule/<calendar_slug>', 
        RoomView.as_view(template_name="detail_room.html"),
        name="tri_month_calendar",
        kwargs={"period": Month},
    )
]
