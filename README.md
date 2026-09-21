# Portfolio Rémy Crespel

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

## Si vous souhaitez lancer l'application directement avec Python localement (Etapes 2 à 4):

## Etape 2: Création et lancement de l'environnement virtuel Python
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

## Etape 3: Installation des dépendances
```bash
pip install -r requirements.txt
```

## Etape 4: Lancement et vérification de l'application
Lancement de l'application
```bash
python3 ./app/app.py
```

L'application est maintenant lancée sur le port 5000 de votre machine, pour voir le site, accéder au site ainsi lancée sur l'url [http://localhost:5000](http://localhost:5000)

## Si vous souhaitez utiliser le dockerfile (étapes 5 à 8):

## Etape 5: Création de l'image Docker à l'aide du Docker Compose

Dans un terminal à la racine du projet:
```bash
docker build -t portfolio-remy-crespel .
```

## Etape 6: Démarrer l'application
Dans un terminal à la racine du projet:
```bash
docker run -d -p 5000:5000  local-portfolio-remy-crespel
```

## Etape 7: Accéder au site internet ainsi lancer
Dans votre navigateur internet préféré aller à l'adresse suivante pour voir le site au complet: [http://localhost:5000](http://localhost:5000)

N'hésitez pas à regarder toutes les pages du site pour en apprendre plus sur moi !

## Etape 8: Arrêter notre projet

Pour arrêter complètement notre projet
```bash
docker stop local-portfolio-remy-crespel
docker rm local-portfolio-remy-crespel
docker rmi portfolio-remy-crespel
```

# Si vous souhaitez utiliser le Docker Compose (étapes 9 à 11)

## Etape 9: Création du conteneur Docker
Dans votre terminal à la racine du projet lancer la commande suivante:
```bash
docker compose up -d --build
```

## Etape 10: Accéder au site internet ainsi lancer
Dans votre navigateur internet préféré aller à l'adresse suivante pour voir le site au complet: [http://localhost:5000](http://localhost:5000)

N'hésitez pas à regarder toutes les pages du site pour en apprendre plus sur moi !

## Etape 11: Arrêter le conteneur lancer précédemment
Pour arrêter complètement notre projet
```bash
docker compose down
```

Si vous voulez relancer le projet, [revenez à l'étape 9](#etape-6-création-du-conteneur-docker)