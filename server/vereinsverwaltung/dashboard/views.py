from django.shortcuts import render
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_overview(request):
	return TemplateResponse(request, "dashboard.html")