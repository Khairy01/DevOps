import pytest
from django.test import RequestFactory
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from WeBib.views import visit_count_api
from WeBib.serializers import VisitSerializer
from django.contrib.sessions.middleware import SessionMiddleware

@pytest.mark.django_db
def test_visit_count_api():
    factory = RequestFactory()

    request = factory.get('/api/visit-count')
    
    middleware = SessionMiddleware(lambda request: None)
    middleware.process_request(request)
    request.session.save()

    response = visit_count_api(request)

    assert response.status_code == HTTP_200_OK

    assert 'visit_count' in response.data

    assert response.data['visit_count'] >= 0

@pytest.mark.django_db
def test_visit_count_api_invalid_data():
    factory = RequestFactory()

    request = factory.post('/api/visit-count')
    response = visit_count_api(request)

    assert response.status_code == 405

    assert 'visit_count' not in response.data
