import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User 

client = APIClient()

@pytest.mark.django_db
def test_status_code():
    url = reverse('user_list')  

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_format_response():
    url = reverse('user_list')  

    response = client.get(url)

    assert response.accepted_media_type == 'application/json'    


@pytest.mark.django_db
def test_invalid_endpoint():

    response = client.get('/api/users/nonexistent/')

    assert response.status_code == 404


