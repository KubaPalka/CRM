from django.urls import path
from . import views

app_name = 'crm_app'

urlpatterns = [
    path('', views.login_user_view, name='login'),
    path('main/', views.MainPageView.as_view(), name='main'),
    path('logout/', views.logout_view, name='logout'),
    path('company_list/', views.CompanyListView.as_view(), name='company-list'),
    path('details/<int:company_id>/', views.CompanyDetailsView.as_view(), name='company-details'),
    path('add_company/', views.CompanyCreate.as_view(), name='add-company'),
    path('edit/<int:company_id>/', views.CompanyEditView.as_view(), name='edit-company'),
    path('delete/<int:company_id>/', views.CompanyDeleteView.as_view(), name='delete-company'),
    path('add_person/<int:company_id>/', views.AddPersonView.as_view(), name='add-person'),
    path('edit_person/<int:company_id>/', views.PersonEditView.as_view(), name='edit-person'),
    path('search_company/', views.SearchCompanyView.as_view(), name="search-company"),
    path('applications/', views.ApplicationCreate.as_view(), name='application-list'),
    path('import_export/', views.DataImportExportView.as_view(), name='import-export'),

]
