from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
from .resources import CompanyDataImportExport


# Register your models here.
@admin.register(models.Company)
class CompanyAdmin(ImportExportModelAdmin):
    resource_class = CompanyDataImportExport


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    model = models.Person


@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    model = models.Branch


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    model = models.Application


@admin.register(models.LegalForm)
class LegalFormAdmin(admin.ModelAdmin):
    model = models.LegalForm
