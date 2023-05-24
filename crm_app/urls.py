from django.urls import path

from . import views

app_name = 'crm_app'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('main/', views.MainPageView.as_view(), name='main'),

]