# Garage V.Parrot - Guide d'installation

## Configuration requise

- Python 3.x
- Pip (gestionnaire de paquets Python)
- PostgreSQL

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/s-dev26/VParrot-Django.git
cd VParrot-Django
```

### 2. Créer un environnement virtuel (recommandé)

```bash
python3 -m venv env
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données

- Installer PostgreSQL
- Suivez les instructions pour installer PostgreSQL. Vous pouvez utiliser Homebrew :

```bash
brew install postgresql
```

### 5. Créer la base de données

```bash
createdb nom_de_la_base_de_données
```

### 6. Créer un fichier .env à la racine du projet et ajouter les informations suivantes :

DEBUG=True
SECRET_KEY=your_secret_key
DJANGO_DB_NAME=nom_de_la_base_de_données
DJANGO_DB_USER=nom_de_l'utilisateur
DJANGO_DB_PASSWORD=your_db_password
DJANGO_DB_HOST=localhost
DJANGO_DB_PORT=5432

### 7. Appliquer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

Suivez les instructions pour créer un administrateur avec un nom d'utilisateur, un email et un mot de passe.

### 9. Lancer le serveur de développement

```bash
python manage.py runserver
```
