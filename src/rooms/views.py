from schedule.views import CalendarByPeriodsView
from rooms.models import RoomImage, Room
from locations.models import Location
from schedule.models import CalendarRelation, Event
from django.conf import settings
from django.views.generic.list import ListView
from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from .forms import BookingForm
from django.db.models import Q
from datetime import datetime
import pytz

class FormListView(FormMixin, ListView):
    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        # From BaseListView
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})

        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

class RoomView(CalendarByPeriodsView):
    # override the "tri_month_calendar" from the "schedule" app
    model = Room
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["room_images"] = self.object.get_room_images()
        # context["parent_location"] = self.object.get_parent_location()
        context["phone_number"] = settings.COMMERCIAL_PHONE_NUMBER
        return context

class RoomsListView(FormListView):
    model = Room
    form_class = BookingForm
    paginate_by = 10 

    def rooms_to_exclude(self, form_data):
        persons = int(form_data["adults"]) + int(form_data["children"])
        timezone = pytz.timezone(settings.TIME_ZONE)
        check_in = timezone.localize(datetime.strptime(form_data["check_in"], "%Y-%m-%d"))
        check_out = timezone.localize(datetime.strptime(form_data["check_out"], "%Y-%m-%d"))
        queryset_list = Event.objects.all()
        room_cap = [(r.calendar_ptr_id, r.max_capacity()) for r in Room.objects.all()]
        return [e.calendar_id for e in queryset_list if len(e._get_occurrence_list(check_in, check_out))>0] + [id for (id, cap) in room_cap if persons>cap]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        form_data = self.form.data
        if len(form_data) == 0:
            return context
        rooms_to_exclude = self.rooms_to_exclude(form_data)
        context["object_list"] = Room.objects.all().exclude(calendar_ptr_id__in = rooms_to_exclude)
        return context
    
