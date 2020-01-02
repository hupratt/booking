from django.conf.urls import url
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path
from . import views
from schedule.periods import Day, Month, Week, Year
from schedule.views import CalendarByPeriodsView
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    path(_('about'), views.AboutView.as_view(), name='about'), 
    path(_('<slug:slug>'), views.detail, name="detail"),

]
