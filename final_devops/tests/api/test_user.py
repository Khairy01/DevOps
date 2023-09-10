import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from WeBib.models import User

client = APIClient()

@pytest.mark.django_db
def test_list_user():
    # test data
    User.objects.create(username="JohnD", email="john@example.com", first_name="John", last_name="Doe")
    User.objects.create(username="JaneS", email="jane@example.com", first_name="Jane", last_name="Smith")

    # URL de l'API pour la liste des utilisateurs
    url = reverse('user_list')  

    #  Requête GET vers l'API
    response = client.get(url)

    #  Réponse a un statut HTTP 200 (OK)
    assert response.status_code == status.HTTP_200_OK

    #  Réponse contient les données attendues
    assert len(response.data) == 2 
    assert response.data[0]['username'] == 'JohnD' 
    assert response.data[1]['username'] == 'JaneS'


@pytest.mark.django_db
def test_invalid_endpoint():
    response = client.get('/api/users/nonexistent/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_invalid_http_method():
    response = client.post('/api/users/')
    assert response.status_code == 404
