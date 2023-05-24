from django.urls import path

from . import views

app_name = 'crm_app'

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),

]