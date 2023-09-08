
# Create your views here.
import base64
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .models import *
import requests


def view_accueil_user(request):
    return render(request,"page_accueil_user.html")
  
def view_accueil_admin(request):
    return render(request,"page_accueil_admin.html")

def view_liste_utilisateurs(request):
    # Remplacez "YOUR_USERNAME" et "YOUR_PASSWORD" par vos informations d'authentification
    username = "admin"
    password = "mars"
    
    # authentification http request
    headers = {
        "Authorization": f"Basic {base64.b64encode(f'{username}:{password}'.encode()).decode()}"
    }
  
    api_url = "https://127.0.0.1:8000/users/"
    response = requests.get(api_url,headers=headers)
    utilisateurs = response.json()  # Si l'API renvoie des données JSON

    return render(request, 'page_list_users.html', {'utilisateurs': utilisateurs})
  
def view_nombre_visiteurs(request):
    # Récupérez le compteur mis à jour(fait par Sougou)
    compteur = 456 #C'est juste un exemple

    return render(request, 'page_nombre_visite.html', {'compteur': compteur})