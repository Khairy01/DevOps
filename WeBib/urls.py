from django.urls import path
from .views import view_liste_utilisateurs, home_view, view_accueil_admin

urlpatterns = [
    path("list_users/", view_liste_utilisateurs, name="list_users"),
    path("number_visits/", home_view, name="number_visits"),
    path("accueil_admin/", view_accueil_admin, name="accueil_admin"),
]
