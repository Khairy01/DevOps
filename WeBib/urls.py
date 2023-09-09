from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list_users/', view_liste_utilisateurs, name='list_users'),
    path('number_visits/', home_view, name='number_visits'),
    path('accueil_admin/', view_accueil_admin, name = 'accueil_admin'),
    
]