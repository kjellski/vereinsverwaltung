from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect
from django.contrib import messages



# Create your views here.
def banking_overview(request):
    return TemplateResponse(request, "banking_overview.html", { "foo": "bar" })