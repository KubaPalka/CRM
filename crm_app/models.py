from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import validate_nip_number


class Company(models.Model):
    name = models.CharField(max_length=128)
    nip = models.IntegerField(unique=True, validators=[validate_nip_number], help_text='wpisz NIP bez myślników')
    address = models.CharField(max_length=128)
    url_site = models.URLField(max_length=64)
    score = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='wartość musi być z przedziału 0-100')
    income = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()
    updated = models.DateField()

    def __str__(self):
        return self.name
