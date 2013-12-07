from django import forms

class MemberForm(forms.Form):
    forename = forms.CharField(label="Vorname")
    surname = forms.CharField(label="Nachname")
    phone = forms.CharField(label="Telefon")
    email = forms.CharField(label="E-Mail")
    street = forms.CharField(label="Straße")
    number = forms.CharField(label="Hausnummer")
    plz = forms.CharField(label="Postleitzahl")
    city = forms.CharField(label="Stadt")
    country = forms.CharField(label="Land")
    iban = forms.CharField(label="IBAN")
    bic = forms.CharField(label="BIC")
    next_pay_date = forms.CharField(label="Nächster Zahlungstermin")
    yearly_amount = forms.CharField(label="Jahresbeitrag")
