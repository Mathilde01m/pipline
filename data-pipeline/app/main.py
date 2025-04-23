from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import psycopg2
from fastapi.middleware.cors import CORSMiddleware

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

try:
    model = joblib.load("iris_model.pkl")
except Exception as e:
    raise RuntimeError(f"Erreur de chargement du modèle : {e}")

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
