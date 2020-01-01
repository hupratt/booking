from django.shortcuts import render
from django.views.generic import ListView
import datetime, pytz
from .models import Location, LocationImage
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from schedule.models import CalendarRelation
from django.conf import settings

# Create your views here.

class AboutView(ListView):
    model = Location
    template_name = "about.html"
    context_object_name = 'about_us_with_properties'

    def get_context_data(self, **kwargs):
        from django.utils.translation import get_language

        context = super().get_context_data(**kwargs)
        language = get_language()
        liste_events_en = Location.objects.all().filter(tag='property').order_by('timestamp')
        if language == 'en':
            context['properties'] = liste_events_en
        else:
            import sys
            sys.path.append("..")
            from booking.translate import translate
            context['properties'] = translate(liste_events_en, language)
        return context

def detail(request, slug):
    """
    Locations method: display the location's detail and associated rooms

    """
    post = get_object_or_404(Location, slug=slug)
    from django.utils.translation import get_language

    language = get_language()
    import sys

    sys.path.append("..")
    from booking.translate import translate

    img_list = LocationImage.objects.filter(location=post)  
    rooms_list = CalendarRelation.objects.filter(object_id=post.id)
    if language == "en":
        context = {
            "post": post,
            "month_year": post.timestamp.strftime("%B, %Y"),
            "img_list": img_list,
            "rooms_list": rooms_list,
            "phone_number": settings.COMMERCIAL_PHONE_NUMBER
        }
    else:
        context = {
            "post": translate(post, language),
            "month_year": post.timestamp.strftime("%B, %Y"),
            "img_list": img_list,
            "rooms_list": rooms_list,
            "phone_number": settings.COMMERCIAL_PHONE_NUMBER
        }
    return render(request, "detail_location.html", context)  # queryset