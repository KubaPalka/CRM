from import_export import resources
from .models import Company


class CompanyDataImportExport(resources.ModelResource):
    class Meta:
        model = Company
        fields = ('id', 'name', 'nip', 'address', 'url_site', 'score', 'income', 'legal_form', 'description', 'user')
        ignore_empty_rows = True


