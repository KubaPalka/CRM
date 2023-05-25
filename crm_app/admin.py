from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    model = models.Company

