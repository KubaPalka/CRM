from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    model = models.Company


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    model = models.Person


@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    model = models.Branch

@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    model = models.Application

