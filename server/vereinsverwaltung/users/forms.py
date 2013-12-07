from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from registration.forms import RegistrationFormUniqueEmail
from django.utils.translation import ugettext as _
from users.models import CustomUser


User = get_user_model()


class CustomRegistrationForm(RegistrationFormUniqueEmail):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label=_("Username"),
                                error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")},
                                help_text=_("Username is visible to all and must not be the same as e-mail address"))
    email = forms.EmailField(label=_('Email'), required=True)
    city = forms.CharField(label=_('City'), max_length=50, required=False)

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']

    def clean(self):
        if 'username' in self.cleaned_data and 'email' in self.cleaned_data:
            if self.cleaned_data['username'] == self.cleaned_data['email']:
                raise forms.ValidationError(_("Username and E-mail should not be the same"))
        return self.cleaned_data

