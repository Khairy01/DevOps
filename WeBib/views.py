from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer,VisitSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import status
from .models import User

# Create your views here.
@api_view(['GET'])
def user_list(request):
    """
    API endpoint that allows users to be viewed.
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def increment_visit_count(request):
    # Récupérez le compteur de visites de la session
    visit_count = request.session.get('visit_count', 0)
    
    # Incrémentez le compteur de visites
    visit_count += 1
    
    # Enregistrez le nouveau compteur dans la session
    request.session['visit_count'] = visit_count
    
    return visit_count

def home_view(request):
    visit_count = increment_visit_count(request)
    return render(request, 'home.html', {'visit_count': visit_count})

@api_view(['GET'])
def visit_count_api(request):
    """
    API endpoint that allows number of visitors to be viewed.
    """
    visit_count = request.session.get('visit_count', 0)
    data = {'visit_count': visit_count}
    serializer = VisitSerializer(data)
    return Response(serializer.data)

