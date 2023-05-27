from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from crm_app import forms
from .models import Company
from .forms import SelectCompanyForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


class MainPageView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'crm_app/main.html')


class CompanyListView(LoginRequiredMixin, View):
    def get(self, request):
        form = SelectCompanyForm()
        return render(request, 'crm_app/company_list.html', {'form': form})

    def post(self, request):
        form = SelectCompanyForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data.get('choice')
            if choice == '1':
                companies = Company.objects.all().order_by('name')
                return render(request, 'crm_app/company_list.html', {'form': form, 'companies': companies})
            elif choice == '2':
                companies = Company.objects.filter(score__gte= 67).filter(income__gte=4000000)
                return render(request, 'crm_app/company_list.html', {'form': form, 'companies': companies})
            elif choice == '3':
                companies = Company.objects.filter(score__lt=67)
                return render(request, 'crm_app/company_list.html', {'form': form, 'companies': companies})
        return render(request, 'crm_app/company_list.html', {'form': form})


class CompanyListAllView(LoginRequiredMixin, View):
    def get(self, request):
        companies = Company.objects.all()
        return render(request, 'crm_app/company_list_all.html', {'companies': companies})


class AddCompanyView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'crm_app/add_company.html')


class DataImportExportView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'crm_app/import_export.html')

class ApplicationListView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'crm_app/applications.html')


def login_user_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, f'Jesteś zalogowany. Witaj {username}!')
                    return redirect(request.GET.get('next', reverse('crm_app:main')))
    else:
        form = forms.LoginForm()
    return render(request, 'crm_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('crm_app:login'))
