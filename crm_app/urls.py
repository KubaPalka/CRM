from django.urls import path
from . import views

app_name = 'crm_app'

urlpatterns = [
    path('', views.login_user_view, name='login'),
    path('main/', views.MainPageView.as_view(), name='main'),
    path('logout/', views.logout_view, name='logout'),
    path('company_list/', views.CompanyListView.as_view(), name='company-list'),
    path('add_company/', views.AddCompanyView.as_view(), name='add-company'),
    path('import_export/', views.DataImportExportView.as_view(), name='import-export'),

]
