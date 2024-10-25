"""Booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path # pylint: disable=no-name-in-module
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    
]
def trigger_error(request):
    division_by_zero = 1 / 0
urlpatterns += i18n_patterns(
    path('', TemplateView.as_view(template_name="intro.html"), name='intro'), 
    path(_('locations/'), include('locations.urls')),
    path(_('rooms/'), include('rooms.urls')),
    path('sentry-debug/', trigger_error),
    prefix_default_language=True)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
