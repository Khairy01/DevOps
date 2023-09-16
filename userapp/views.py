from django.shortcuts import render, redirect
from userapp.forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.user.is_superuser:
        return render(request, "page_accueil_admin.html")
    else:
        return render(request, "page_accueil_user.html")


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, f"Coucou {username}, Votre compte a été créé avec succès !"
            )
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})
