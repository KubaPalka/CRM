from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import validate_nip_number
from django.utils import timezone


class Company(models.Model):
    """
    Represents a model for storing information about a company
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    nip = models.CharField(unique=True, validators=[validate_nip_number], help_text='wpisz NIP bez myślników')
    address = models.CharField(max_length=128)
    url_site = models.URLField(max_length=64)
    score = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                     help_text='wartość musi być z przedziału 0-100')
    income = models.IntegerField()
    legal_form = models.ForeignKey('LegalForm', on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()
    updated = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Person(models.Model):
    """
    Represents a model for storing information about a companies' employees
    """
    full_name = models.CharField(max_length=64)
    email = models.EmailField(blank=True, default=None)
    phone = models.CharField(max_length=16)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Branch(models.Model):
    """
    Represents a model for storing information about branches connected with companies
    """
    OPTIONS = (
        ('administracja', 'administracja'),
        ('budownictwo', 'budownictwo'),
        ('handel', 'handel'),
        ('IT', 'IT'),
        ('ochrona zdrowia', 'ochrona zdrowia'),
        ('produkcja', 'produkcja'),
        ('przemysł', 'przemysł'),
        ('transport', 'transport'),
        ('usługi', 'usługi'),
        ('inne', 'inne')
    )
    name = models.CharField(max_length=32, choices=OPTIONS)
    companies = models.ManyToManyField(Company, related_name='branches')

    def __str__(self):
        return self.name


class LegalForm(models.Model):
    """
    Represents a model for storing information about company's legal form
    """
    OPTIONS = (
        ('spółka akcyjna', 'spółka akcyjna'),
        ('spółka z o.o.', 'spółka z o.o.'),
        ('spółka komandytowa', 'spółka komandytowa'),
        ('spółka jawna', 'spółka jawna'),
        ('spółka cywilna', 'spółka cywilna'),
        ('1-os. DG', '1-os. DG'),
        ('spółdzielnia', 'spółdzielnia'),
        ('spółka komunalna', 'spółka komunalna'),
        ('wspólnota', 'wspólnota'),
        ('inna', 'inna')
    )
    name = models.CharField(max_length=32, choices=OPTIONS)

    def __str__(self):
        return self.name


class Application(models.Model):
    """
    Represents a model for storing information about a company's active applications for a solar installation
    """
    OPTIONS = (
        ('Seraphim', 'Seraphim'),
        ('JA solar', 'JA solar'),
        ('Jinko', 'Jinko'),
        ('AE Solar', 'AE Solar'),
        ('Longi', 'Longi'),
        ('Trina', 'Trina'),
        ('Risen', 'Risen')
    )
    TYPES = (
        ('Skośny', 'Skośny'),
        ('Ekierka', 'Ekierka'),
        ('Balast WZ', 'Balast WZ'),
        ('Balast południe', 'Balast południe'),
        ('Klejona WZ', 'Klejona WZ'),
        ('Klejona Południe', 'Klejona Południe'),
        ('Grunt Mono', 'Grunt Mono'),
        ('Grunt Bifacial', 'Grunt Bifacial'),
        ('Carport Standard', 'Carport Standard'),
        ('Carport Premium', 'Carport Premium')
    )
    PAYMENTS = (
        ('SUSI', 'SUSI'),
        ('Leasing', 'Leasing'),
        ('Kredyt', 'Kredyt'),
        ('Gotówka', 'Gotówka')
    )
    STATUS = (
        ('złożony', 'złożony'),
        ('umowa', 'umowa'),
        ('wypłata', 'wypłata'),
        ('rezygnacja', 'rezygnacja')
    )
    app_number = models.CharField(max_length=16)
    kwh_amount = models.SmallIntegerField(validators=[MinValueValidator(0)])
    installation_type = models.CharField(max_length=32, choices=TYPES)
    panel_type = models.CharField(max_length=32, choices=OPTIONS)
    payment = models.CharField(max_length=32, choices=PAYMENTS)
    status = models.CharField(max_length=16, choices=STATUS)
    date_added = models.DateField(auto_now_add=True)
    updated = models.DateField(default=timezone.now)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.app_number

