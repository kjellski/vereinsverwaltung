from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
# Create your views here.

def home(request):
	return TemplateResponse(request, "home.html")