from django.conf.urls import *
from django.views.generic import TemplateView
from .views import *



urlpatterns = patterns('',
                       url(r'^login/$', user_login, name='user_login'),

)