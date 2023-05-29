from django import forms
from django.core.exceptions import ValidationError


def validate_nip_number(nip):
    if len(nip) != 10:
        raise ValidationError("NIP powinien mieć 10 cyfr!")
    if not nip.isdigit():
        raise ValidationError("NIP może zawierać tylko cyfry!")
    wages = (6, 5, 7, 2, 3, 4, 5, 6, 7)
    checksum = sum(int(nip[i]) * wages[i] for i in range(9))
    if not checksum % 11 == int(nip[-1]):
        raise ValidationError("Numer NIP jest niepoprawny!")
