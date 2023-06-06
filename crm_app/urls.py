from django.urls import path
from . import views

app_name = 'crm_app'

urlpatterns = [
    path('', views.login_user_view, name='login'),
    path('main/', views.MainPageView.as_view(), name='main'),
    path('logout/', views.logout_view, name='logout'),
    path('change_password/', views.UserPasswordChangeView.as_view(), name='change-password'),
    path('company_list/', views.CompanyListView.as_view(), name='company-list'),
    path('details/<int:company_id>/', views.CompanyDetailsView.as_view(), name='company-details'),
    path('add_company/', views.CompanyCreate.as_view(), name='add-company'),
    path('edit/<int:company_id>/', views.CompanyEditView.as_view(), name='edit-company'),
    path('delete/<int:company_id>/', views.CompanyDeleteView.as_view(), name='delete-company'),
    path('add_person/<int:company_id>/', views.AddPersonView.as_view(), name='add-person'),
    path('edit_person/<int:company_id>/', views.PersonEditView.as_view(), name='edit-person'),
    path('search_company/', views.SearchCompanyView.as_view(), name='search-company'),
    path('applications/', views.ApplicationListView.as_view(), name='application-list'),
    path('application_details/<int:application_id>/', views.ApplicationDetailsView.as_view(),
         name='application-details'),
    path('add_application/', views.ApplicationCreate.as_view(), name='add-application'),
    path('edit_application/<int:application_id>/', views.ApplicationEditView.as_view(), name='edit-application'),
    path('import_export/', views.DataImportExportView.as_view(), name='import-export'),

]
