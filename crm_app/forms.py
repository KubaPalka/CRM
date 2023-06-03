from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from . import models
from .models import Company, Person, Application


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nazwa użytkownika', widget=forms.TextInput(attrs={'name': 'username'}))
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

    class Meta:
        fields = ('username', 'password')

    error_messages = {'invalid_login': 'Email lub/i hasło nie pasują do żadnego użytkownika.'}


class SelectCompanyForm(forms.Form):
    OPTIONS = (
        (1, 'Wszystkie'),
        (2, 'SUSI'),
        (3, 'Pozostałe')
    )
    choice = forms.ChoiceField(label='Wybierz:', choices=OPTIONS, widget=forms.RadioSelect)


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'nip', 'address', 'url_site', 'score', 'income', 'legal_form', 'description']
        labels = {'name': 'Nazwa', 'nip': 'NIP', 'address': 'Adres', 'url_site': 'WWW',
                  'score': 'Punktacja SUSI', 'income': 'Przychód', 'legal_form': 'Forma prawna', 'description': 'Opis'}


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = {'full_name', 'email', 'phone'}
        labels = {'full_name': 'Nazwisko i imię', 'email': 'Email', 'phone': 'Telefon'}


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = {'app_number', 'kwh_amount', 'installation_type', 'panel_type', 'payment', 'status',
                  'updated', 'company'}
        labels = {'app_number': 'Numer wniosku', 'kwh_amount': 'Moc instalacji w kWh',
                  'installation_type': 'Rodzaj instalacji', 'panel_type': 'Panele',
                  'payment': 'Finansowanie', 'status': 'Status wniosku', 'update': 'Aktualizacja', 'company': 'Firma'}
