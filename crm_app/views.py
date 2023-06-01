from django.db.models import Q
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from crm_app import forms
from .models import Company, Person, Branch
from .forms import SelectCompanyForm, CompanyForm, PersonForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView



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
                no_of_companies = companies.count()
                return render(request, 'crm_app/company_list.html', {'form': form, 'companies': companies,
                                                                     'no_of_companies': no_of_companies})
            elif choice == '2':
                companies = Company.objects.filter(score__gte=67, income__gte=4000000)
                no_of_companies = companies.count()
                return render(request, 'crm_app/company_list.html', {'form': form, 'companies': companies,
                                                                     'no_of_companies': no_of_companies})
            elif choice == '3':
                companies = Company.objects.filter(Q(score__lt=67) | Q(income__lt=4000000))
                no_of_companies = companies.count()
                return render(request, 'crm_app/company_list.html', {'form': form, 'companies': companies,
                                                                     'no_of_companies': no_of_companies})
        return render(request, 'crm_app/company_list.html', {'form': form})


class CompanyDetailsView(LoginRequiredMixin, View):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(pk=company_id)
            branches = company.branches.all()
            try:
                person = Person.objects.get(pk=company_id)
            except Person.DoesNotExist:
                person = None
            return render(request, 'crm_app/company_details.html', {'company': company, 'person': person,
                                                                    'branches': branches})
        except Company.DoesNotExist:
            return render(request, 'crm_app/company_details.html')



class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('crm_app:company-list')

class CompanyEditView(View):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(pk=company_id)
            return render(request, 'crm_app/company_edit.html', {'company': company})
        except Company.DoesNotExist:
            return render(request, 'crm_app/company_edit.html')

class CompanyDeleteView(View):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(pk=company_id)
            return render(request, 'crm_app/company_delete.html', {'company': company})
        except Company.DoesNotExist:
            return render(request, 'crm_app/company_delete.html')


class SearchCompanyView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'crm_app/search_company.html')

class AddPersonView(LoginRequiredMixin, View):
    def get(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        form = PersonForm()
        return render(request, 'crm_app/add_person.html', {'company': company, 'form': form})
    def post(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        form = PersonForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            Person.objects.create(full_name=full_name, email=email, phone=phone, company_id=company_id)
            msg = 'Pomyślnie dodano osobę do kontaktu.'
            return render(request, 'crm_app/add_person.html', {'company': company, 'form': form, 'msg': msg})
        return render(request, 'crm_app/add_person.html', {'company': company, 'form': form})





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
