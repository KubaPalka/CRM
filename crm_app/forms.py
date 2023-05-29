from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from . import models


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nazwa użytkownika', widget=forms.TextInput(attrs={'name': 'username'}))
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

    class Meta:
        fields = ('username', 'password')

    error_messages = {
        "invalid_login": "Email lub/i hasło nie pasują do żadnego użytkownika."
    }


class SelectCompanyForm(forms.Form):
    OPTIONS = (
        (1, "Wszystkie"),
        (2, "SUSI"),
        (3, "Pozostałe")
    )
    choice = forms.ChoiceField(label="Wybierz:", choices=OPTIONS, widget=forms.RadioSelect)
