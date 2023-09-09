
# Create your views here.
import base64
from .models import *
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .serializers import UserSerializer,VisitSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import status


def view_accueil_user(request):
    return render(request,"page_accueil_user.html")
  
def view_accueil_admin(request):
    return render(request,"page_accueil_admin.html")

def view_liste_utilisateurs(request):
    api_url = "http://127.0.0.1:8000/api/user/"
    response = requests.get(api_url)
    utilisateurs = response.json()  # Si l'API renvoie des données JSON

    return render(request, 'page_list_users.html', {'utilisateurs': utilisateurs})



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
    return render(request, 'page_nombre_visite.html', {'visit_count': visit_count})

@api_view(['GET'])
def visit_count_api(request):
    """
    API endpoint that allows number of visitors to be viewed.
    """
    visit_count = request.session.get('visit_count', 0)
    data = {'visit_count': visit_count}
    serializer = VisitSerializer(data=data)  # Instanciez le sérialiseur avec les données
    if serializer.is_valid():  # Vérifiez si le sérialiseur est valide
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)  # Si le sérialiseur n'est pas valide, renvoyez une réponse d'erreur 400
