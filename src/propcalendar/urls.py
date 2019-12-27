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


urlpatterns = [
    path('', TemplateView.as_view(template_name="calendar/homepage.html"),),
    path('schedule/', include('schedule.urls')),
    path('fullcalendar/', TemplateView.as_view(template_name="calendar/fullcalendar.html"), name='fullcalendar'),
    path('schedule/<calendar_slug>/', 
        CalendarByPeriodsView.as_view(template_name="calendar/calendar_tri_month.html"),
        name="tri_month_calendar",
        kwargs={"period": Month},
    )
]
