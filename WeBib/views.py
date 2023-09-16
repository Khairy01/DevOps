# Create your views here.
from .models import Visit
from django.contrib.auth.models import User
import requests
from django.shortcuts import render
from .serializers import UserSerializer, VisitSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


def view_accueil_user(request):
    return render(request, "page_accueil_user.html")


def view_accueil_admin(request):
    return render(request, "page_accueil_admin.html")


def view_liste_utilisateurs(request):
    api_url = "http://127.0.0.1:8000/api/user/"
    response = requests.get(api_url)
    utilisateurs = response.json()

    return render(request, "page_list_users.html", {"utilisateurs": utilisateurs})


@api_view(["GET"])
def user_list(request):
    """
    API endpoint that allows users to be viewed.
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def home_view(request):
    api_url = "http://127.0.0.1:80/api/visit-count/"
    response = requests.get(api_url)
    visit = response.json()
    return render(request, "page_nombre_visite.html", {"visit_count": visit})


@api_view(["GET"])
def visit_count(request):
    """
    API endpoint that allows number of visitors to be viewed.
    """
    visit = Visit.objects.first()
    if not visit:
        visit = Visit.objects.create()
    visit.count += 1
    visit.save()

    serializer = VisitSerializer(visit)
    return Response(serializer.data)
