from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from registration.forms import RegistrationFormUniqueEmail
from django.utils.translation import ugettext as _
from users.models import CustomUser

