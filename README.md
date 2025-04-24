# Data Pipeline Project

Ce projet met en place un pipeline de données avec FastAPI, Docker, PostgreSQL et MLflow. Il permet d'entraîner un modèle de prédiction pour la longueur du sépale d'iris à partir de la largeur du sépale. L'API exposée permet d'insérer des données dans une base PostgreSQL, d'entraîner un modèle et de faire des prédictions via une API REST.

## Prérequis

Avant de commencer, assure-toi que tu as les éléments suivants installés :

- Docker et Docker Compose
- Python 3.x
- pip (gestionnaire de paquets Python)

## Structure du projet

Le projet est divisé en plusieurs services, chacun étant un conteneur Docker :

- **FastAPI (API)** : L'API REST pour insérer des données et effectuer des prédictions.
- **PostgreSQL** : Base de données pour stocker les données d'iris.
- **MLflow** : Outil pour la gestion du modèle de machine learning.
- **Train** : Service pour entraîner le modèle de prédiction sur les données.

### Détails des services :

1. **FastAPI (API)** : Ce service permet de faire des requêtes pour insérer des données dans PostgreSQL et d'effectuer des prédictions avec le modèle d'iris.
2. **PostgreSQL** : Contient les données d'entraînement pour le modèle.
3. **MLflow** : Permet de suivre les expériences de machine learning et de gérer les modèles.
4. **Train** : Service pour entraîner le modèle avec les données d'iris.

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/ton-organisation/data-pipeline.git
cd data-pipeline
