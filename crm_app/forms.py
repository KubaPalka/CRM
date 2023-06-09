from django import forms
from django.contrib.auth import password_validation

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from . import models
from .models import Company, Person, Application, LegalForm


class LoginForm(AuthenticationForm):
    """
    Form used for user authentication in based on the AuthenticationForm
    """
    username = forms.CharField(label='Nazwa użytkownika', widget=forms.TextInput(attrs={'name': 'username'}))
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

    class Meta:
        fields = ('username', 'password')

    error_messages = {'invalid_login': 'Email lub/i hasło nie pasują do żadnego użytkownika.'}


class SelectCompanyForm(forms.Form):
    """
    Form used for basic companies selection
    """
    OPTIONS = (
        (1, 'Wszystkie'),
        (2, 'SUSI'),
        (3, 'Pozostałe')
    )
    choice = forms.ChoiceField(label='Wybierz:', choices=OPTIONS, widget=forms.RadioSelect)


class CompanyForm(forms.ModelForm):
    """
    Form used for creating and editing records base on Company model
    """
    class Meta:
        model = Company
        fields = ['name', 'nip', 'address', 'url_site', 'score', 'income', 'legal_form', 'description']
        labels = {'name': 'Nazwa', 'nip': 'NIP', 'address': 'Adres', 'url_site': 'WWW',
                  'score': 'Punktacja SUSI', 'income': 'Przychód', 'legal_form': 'Forma prawna', 'description': 'Opis'}


class PersonForm(forms.ModelForm):
    """
    Form used for creating and editing records base on Person model
    """
    class Meta:
        model = Person
        fields = {'full_name', 'email', 'phone'}
        labels = {'full_name': 'Nazwisko i imię', 'email': 'Email', 'phone': 'Telefon'}


class ApplicationForm(forms.ModelForm):
    """
    Form used for creating and editing records base on Application model
    """
    class Meta:
        model = Application
        fields = {'app_number', 'kwh_amount', 'installation_type', 'panel_type', 'payment', 'status',
                  'updated', 'company'}
        labels = {'app_number': 'Numer wniosku', 'kwh_amount': 'Moc instalacji w kWh',
                  'installation_type': 'Rodzaj instalacji', 'panel_type': 'Panele',
                  'payment': 'Finansowanie', 'status': 'Status wniosku', 'update': 'Aktualizacja', 'company': 'Firma'}


class CompanySearchForm(forms.Form):
    """
    Form used for searching companies based on mutlitple filters
    """
    name = forms.CharField(required=False, label='Nazwa firmy:')
    nip = forms.CharField(required=False, label="NIP:")
    score = forms.IntegerField(required=False, label="Punktacja od:")
    income = forms.IntegerField(required=False, label='Przychód od:')
    legal_form = forms.ModelChoiceField(queryset=LegalForm.objects.all(), empty_label='', required=False,
                                        label='Forma prawna:')


class UserPasswordChangeForm(PasswordChangeForm):
    """
    Form used for user password change based od PasswordChangeForm
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = "Stare hasło"
        self.fields['new_password1'].label = "Nowe hasło"
        self.fields['new_password2'].label = "Potwierdź nowe hasło"
    error_messages = {'password_mismatch': 'Podane hasła muszą być takie same!',
                      'password_incorrect': 'Aktualne hasło jest nieprawidłowe.'}
