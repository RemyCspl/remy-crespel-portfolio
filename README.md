# Portfolio Rémy Crespel

## Table des matières

- [Comment lancer mon application](#comment-lancer-mon-application)
  - [Prérequis](#prérequis)
    - [Docker Desktop ou docker Engine](#docker-desktop-ou-docker-engine)
    - [Git](#git)
    - [Python si vous voulez lancer l'application localement](#python-si-vous-voulez-lancer-lapplication-localement)
  - [Si vous souhaitez lancer l'application directement avec Python localement](#si-vous-souhaitez-lancer-lapplication-directement-avec-python-localement)
    - [Étape 1: Création et lancement de l'environnement virtuel Python](#etape-1-création-et-lancement-de-lenvironnement-virtuel-python)
    - [Étape 2: Installation des dépendances](#etape-2-installation-des-dépendances)
    - [Étape 3: Lancement et vérification de l'application](#etape-3-lancement-et-vérification-de-lapplication)
  - [Si vous souhaitez utiliser le dockerfile](#si-vous-souhaitez-utiliser-le-dockerfile)
    - [Étape 1: Création de l'image Docker à l'aide du Docker Compose](#etape-1-création-de-limage-docker-à-laide-du-docker-compose)
    - [Étape 2: Démarrer l'application](#etape-2-démarrer-lapplication)
    - [Étape 3: Accéder au site internet ainsi lancer](#etape-3-accéder-au-site-internet-ainsi-lancer)
    - [Étape 4: Arrêter notre projet](#etape-4-arrêter-notre-projet)
  - [Si vous souhaitez utiliser le Docker Compose](#si-vous-souhaitez-utiliser-le-docker-compose)
    - [Étape 1: Création du conteneur Docker](#etape-1-création-du-conteneur-docker)
    - [Étape 2: Accéder au site internet ainsi lancer](#etape-2-accéder-au-site-internet-ainsi-lancer)
    - [Étape 3: Arrêter le conteneur lancer précédemment](#etape-3-arrêter-le-conteneur-lancer-précédemment)

## Comment lancer mon application

## Prérequis

### Docker Desktop ou docker Engine

Pour vérifier si il y a déjà une version de Docker installée sur sa machine, à lancer dans le terminal:
```bash
docker --version
```
La commande doit retouner une valeur du style:
```bash
Docker version 29.7.2
```

Si cela renvoie une erreur: [Installer Docker](https://www.docker.com/get-started/)

### Git

Pour vérifier si il y a déjà une version de Git installée sur sa machine, à lancer dans le terminal:
```bash
git version
```
La commande doit retouner une valeur du style:
```bash
git version 2.55.0.windows.2
```

Si cela renvoie une erreur: [Installer Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

### Python si vous voulez lancer l'application localement
Pour vérifier si il y a déjà une version de Pyhton installée sur sa machine, à lancer dans le terminal:
```bash
python3 --version
```
La commande doit retouner une valeur du style:
```bash
Python 3.14.6
```

## Etape 1: Clonage du repo Git

Dans un terminal:
```bash
git clone https://github.com/RemyCspl/remy-crespel-portfolio
```

## Si vous souhaitez lancer l'application directement avec Python localement:

### Etape 1: Création et lancement de l'environnement virtuel Python
* Création de l'environnement virtuel Python
```bash
python3 -m venv .venv
```

* Activation de l'environnement virtuel
  - Sur Windows (CMD / Invite de commandes) :
   ```bash
    .venv\Scripts\activate.bat
   ```

  - Sur Windows (PowerShell) :
   ```bash
    .venv\Scripts\Activate.ps1
   ```

  - Sur macOS et Linux :
   ```bash
     source .venv/bin/activate
   ```

### Etape 2: Installation des dépendances
```bash
pip install -r requirements.txt
```

### Etape 3: Lancement et vérification de l'application
Lancement de l'application
```bash
python3 ./app/app.py
```

L'application est maintenant lancée sur le port 5000 de votre machine, pour voir le site, accéder au site ainsi lancée sur l'url [http://localhost:5000](http://localhost:5000)

## Si vous souhaitez utiliser le dockerfile:

### Etape 1: Création de l'image Docker à l'aide du Docker Compose

Dans un terminal à la racine du projet:
```bash
docker build -t portfolio-remy-crespel .
```

### Etape 2: Démarrer l'application
Dans un terminal à la racine du projet:
```bash
docker run -d -p 5000:5000  local-portfolio-remy-crespel
```

### Etape 3: Accéder au site internet ainsi lancer
Dans votre navigateur internet préféré aller à l'adresse suivante pour voir le site au complet: [http://localhost:5000](http://localhost:5000)

N'hésitez pas à regarder toutes les pages du site pour en apprendre plus sur moi !

### Etape 4: Arrêter notre projet

Pour arrêter complètement notre projet
```bash
docker stop local-portfolio-remy-crespel
docker rm local-portfolio-remy-crespel
docker rmi portfolio-remy-crespel
```

## Si vous souhaitez utiliser le Docker Compose:

### Etape 1: Création du conteneur Docker
Dans votre terminal à la racine du projet lancer la commande suivante:
```bash
docker compose up -d --build
```

### Etape 2: Accéder au site internet ainsi lancer
Dans votre navigateur internet préféré aller à l'adresse suivante pour voir le site au complet: [http://localhost:5000](http://localhost:5000)

N'hésitez pas à regarder toutes les pages du site pour en apprendre plus sur moi !

### Etape 3: Arrêter le conteneur lancer précédemment
Pour arrêter complètement notre projet
```bash
docker compose down
```

Si vous voulez relancer le projet, [revenez à l'étape 1](#etape-1-création-du-conteneur-docker)