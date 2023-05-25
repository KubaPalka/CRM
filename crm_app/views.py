from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from crm_app import forms


class MainPageView(View):
    def get(self, request):
        return render(request, 'crm_app/main.html')

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