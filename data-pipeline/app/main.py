from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import joblib  # ✅ on utilise joblib maintenant

app = FastAPI()

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float

class PredictInput(BaseModel):
    sepal_width: float

# Connexion à PostgreSQL
conn = psycopg2.connect(
    dbname="irisdb",
    user="irisuser",
    password="irispass",
    host="db",
    port="5432"
)

# ✅ Chargement du modèle local avec joblib
model = joblib.load("iris_model.pkl")

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
