from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from fastapi.middleware.cors import CORSMiddleware
import mlflow.pyfunc
import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float

class PredictInput(BaseModel):
    sepal_width: float

# Connexion PostgreSQL
conn = psycopg2.connect(
    dbname="irisdb",
    user="irisuser",
    password="irispass",
    host="db",
    port="5432"
)

# Chargement du modèle depuis MLflow
MLFLOW_TRACKING_URI = "http://mlflow:5000"
EXPERIMENT_NAME = "iris-regression"
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
runs = mlflow.search_runs(experiment_ids=[experiment.experiment_id], order_by=["start_time desc"])
last_run_id = runs.iloc[0]["run_id"]
model_uri = f"runs:/{last_run_id}/model"
model = mlflow.pyfunc.load_model(model_uri)

@app.get("/")
def root():
    return {"status": "API up and running"}

@app.post("/insert")
def insert_data(data: IrisData):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO iris_data (sepal_length, sepal_width)
            VALUES (%s, %s)
        """, (data.sepal_length, data.sepal_width))
        conn.commit()
    return {"message": "Data inserted"}

@app.post("/predict")
def predict(data: PredictInput):
    prediction = model.predict([[data.sepal_width]])[0]
    return {"sepal_length_predicted": round(prediction, 2)}

# Monter les fichiers statiques
app.mount("/static", StaticFiles(directory="static"), name="static")

# Route pour servir l'interface utilisateur
@app.get("/ui")
def get_ui():
    return FileResponse(os.path.join("static", "index.html"))
