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

## Etape 1: Clonage du repo Git

Dans un terminal:
```bash
git clone https://github.com/RemyCspl/remy-crespel-portfolio
```

## Si vous souhaitez utiliser le dockerfile (étapes 2 à 5):

## Etape 2: Création de l'image Docker à l'aide du Docker Compose

Dans un terminal à la racine du projet:
```bash
docker build -t portfolio-remy-crespel .
```

## Etape 3: Démarrer l'application
Dans un terminal à la racine du projet:
```bash
docker run -d -p 5000:5000  local-portfolio-remy-crespel
```

## Etape 4: Accéder au site internet ainsi lancer
Dans votre navigateur internet préféré aller à l'adresse suivante pour voir le site au complet:
```text
http://localhost:5000
```

N'hésitez pas à regarder toutes les pages du site pour en apprendre plus sur moi !

## Etape 5: Arrêter notre projet

Pour arrêter complètement notre projet
```bash
docker stop local-portfolio-remy-crespel
docker rm local-portfolio-remy-crespel
docker rmi portfolio-remy-crespel
```

# Si vous souhaitez utiliser le Docker Compose (étapes 6 à ...)

## Etape 6: Création du conteneur Docker
Dans votre terminal à la racine du projet lancer la commande suivante:
```bash
docker compose up -d --build
```

## Etape 7: Accéder au site internet ainsi lancer
Dans votre navigateur internet préféré aller à l'adresse suivante pour voir le site au complet:
```text
http://localhost:5000
```

N'hésitez pas à regarder toutes les pages du site pour en apprendre plus sur moi !

## Etape 8: Arrêter le conteneur lancer précédemment
Pour arrêter complètement notre projet
```bash
docker compose down
```

Si vous voulez relancer le projet, [revenez à l'étape 6](#etape-6-création-du-conteneur-docker)