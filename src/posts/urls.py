from django.conf.urls import url
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path # pylint: disable=no-name-in-module
from . import views

urlpatterns = [
    path('about', views.AboutView.as_view(), name='about'), 
    path('<slug:slug>', views.detail, name="detail"),

]
