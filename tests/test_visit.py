import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from WeBib.models import Visit

client = APIClient()


@pytest.mark.django_db
def test_status_code():
    url = reverse("visit_count")

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_format_response():
    url = reverse("visit_count")

    response = client.get(url)

    assert response.accepted_media_type == "application/json"


@pytest.mark.django_db
def test_valid_data():
    url = reverse("visit_count")

    for _ in range(5):
        response = client.get(url)

    assert "count" in response.data

    updated_visit = Visit.objects.first()

    assert response.data["count"] == updated_visit.count


@pytest.mark.django_db
def test_no_visit_object():
    Visit.objects.all().delete()

    url = reverse("visit_count")

    response = client.get(url)

    assert "count" in response.data

    assert response.data["count"] == 1
