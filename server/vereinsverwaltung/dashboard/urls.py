from django.conf.urls import *
from django.views.generic import TemplateView
from .views import *



urlpatterns = patterns('',
                       url(r'^$', dashboard_overview, name='dashboard'),

)