import pytest
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from crm_app.views import ApplicationListView, ApplicationCreate



def test_login_page(client):
    url = reverse('crm_app:login')
    response = client.get(url)
    assert response.status_code == 200
    assert '<h2>Zaloguj się do CRM:</h2>' in response.content.decode('UTF-8')

@pytest.mark.django_db
def test_application_list_view(client):
    user = User.objects.create_user(username='test_user', password='test_password')
    client.login(username='test_user', password='test_pass')
    factory = RequestFactory()
    request = factory.get(reverse('crm_app:application-list'))
    request.user = user
    response = ApplicationListView.as_view()(request)
    assert response.status_code == 200
@pytest.mark.django_db
def test_application_create_view(client):
    user = User.objects.create_user(username='test_user', password='test_password')
    client.login(username='test_user', password='test_password')
    factory = RequestFactory()
    request = factory.get(reverse('crm_app:add-application'))
    request.user = user
    response = ApplicationCreate.as_view()(request)
    assert response.status_code == 200
    assert 'crm_app/application_form.html' in response.template_name
    assert 'form' in response.context_data


