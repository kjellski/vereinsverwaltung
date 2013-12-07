from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect
from .models import CustomUser
from organisations.models import Organisation
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and password is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("dashboard"))
            else:
                messages.error(request, "user is not active")
                return TemplateResponse(request, "login.html")
        else:
            messages.error(request, "login failed")
            return TemplateResponse(request, "login.html")
    else: 
        return TemplateResponse(request, "login.html")

def add_organisation(request):
	return TemplateResponse(request, "")