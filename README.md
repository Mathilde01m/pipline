# 🌸 Iris Data Pipeline – Prédiction ML avec FastAPI, MLflow & Docker

Ce projet met en place un pipeline de modélisation machine learning complet et **dockerisé**, pour prédire la **longueur du sépale** d’une fleur Iris à partir de sa largeur.

Il inclut :
- 🧠 Un modèle RandomForestRegressor entraîné et suivi avec MLflow
- 🔁 Une API REST avec FastAPI pour l’insertion et la prédiction
- 💻 Une interface web simple en HTML/CSS/JS
- 🐳 Un environnement complet sous Docker

---

## 📂 Structure du projet

data-pipeline/ ├── app/ │ ├── main.py # API FastAPI │ ├── Dockerfile # Image pour l'API │ ├── requirements.txt │ └── static/ # Interface web │ ├── index.html │ ├── script.js │ └── styles.css ├── train/ │ ├── train.py # Entraînement + MLflow │ └── Dockerfile # Image d'entraînement ├── iris 1.csv # Données brutes ├── insert.py # Script d'insertion de données ├── docker-compose.yml # Orchestration Docker ├── init.sql # Création de la table iris_data


---

## 🚀 Démarrage rapide

### 1. Cloner le projet

```bash
git clone <repo>
cd data-pipeline
```

## 2. Lancer le pipeline

docker-compose up --build

### Insérer les données dans PostgreSQL

python insert.py

### Lancer l'API
docker-compose up --build  

## 🌐 Interface web

Accessible ici :
👉 http://localhost:8000/ui

Entrez une largeur de sépale

Cliquez sur Prédire

La longueur estimée s’affiche automatiquement 🎉


## 🔁 API FastAPI
### 📥 POST /insert

POST http://localhost:8000/insert
{
  "sepal_length": 5.1,
  "sepal_width": 3.5
}

### 📊 POST /predict

POST http://localhost:8000/predict
{
  "sepal_width": 3.5
}

### 🩺 GET /

curl http://localhost:8000/

### 📈 Suivi des modèles MLflow
Interface web MLflow :
👉 http://localhost:5000

Visualisation des paramètres, métriques et modèles
Historique des expériences
Récupération du meilleur modèle automatiquement dans l’API

### 🛠 Technologies utilisées

Python 3.11
FastAPI & Uvicorn
scikit-learn (RandomForestRegressor)
PostgreSQL
MLflow
Docker & Docker Compose
HTML/CSS/JS (frontend minimal)

### 💡 Idées d'amélioration
⚙️ Scheduler automatique d'entraînement
📦 Export ONNX du modèle
📊 Dashboard Streamlit ou Gradio
🔐 Authentification dans l’interface
📤 Déploiement sur un VPS ou dans le cloud (Render, Heroku, etc.)

### 👩‍💻 Auteurs
Projet développé par Yrieix DE FOUCAULD et Mathilde De Oliveira – Étudiants en Expert(e) en Management des Systèmes d'Information à Epitech Digital School 🎓

### 📜 Licence
Ce projet est open-source. Utilisation libre dans un cadre pédagogique ou personnel.


