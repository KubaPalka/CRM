from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect, reverse

from crm_app import forms


class MainPageView(View):
    def get(self, request):
        return render(request, 'crm_app/main.html')

def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(email=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, f'You are logged in. Hello {username}')
                    return redirect(request.GET.get('next', reverse('crm_app:home')))
    else:
        form = forms.LoginForm()
    return render(request, 'crm_app/login.html', {'form': form})
