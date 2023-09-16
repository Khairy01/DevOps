# Utilisez l'image Python officielle comme image de base
FROM python:3.10

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installez les dépendances Python
RUN pip install -r requirements.txt

# Copiez le reste de votre application dans le conteneur
COPY . .

EXPOSE 8000

# Exécutez la commande pour démarrer votre application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
