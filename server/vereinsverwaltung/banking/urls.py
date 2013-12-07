from django.conf.urls import *
from django.views.generic import TemplateView
from .views import *

urlpatterns = patterns('',
    url(r'^overview/$', banking_overview, name='banking_overview'),
)