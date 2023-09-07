
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .models import *


def view_accueil_user(request):
    return render(request,"page_accueil_user.html")
  
def view_accueil_admin(request):
    return render(request,"page_accueil_admin.html")

def view_liste_utilisateurs(request):
  
    #utilisateurs = Utilisateur.objects.all() # Récupérez tous les utilisateurs de la base de données récupérés à partir de l'inscription
     # Ceci est un text d'utilisateurs; à enlever après
    utilisateurs = [
        Utilisateur(first_name="Doe", last_name="John", username="motdepasse1",email="email1"),
        Utilisateur(first_name="Gueye", last_name="John", username="motdepasse2",email="email2"),
        Utilisateur(first_name="Sall", last_name="John", username="motdepasse3",email="email3"),
    ]
    return render(request, 'page_list_users.html', {'utilisateurs': utilisateurs})
  
def view_nombre_visiteurs(request):
    # Récupérez le compteur mis à jour(fait par Sougou)
    compteur = 456 #C'est juste un exemple

    return render(request, 'page_nombre_visite.html', {'compteur': compteur})