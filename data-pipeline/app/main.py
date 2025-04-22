from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float


conn = psycopg2.connect(
    dbname="irisdb",
    user="irisuser",
    password="irispass",
    host="db",
    port="5432"
)

@app.post("/insert")
def insert_data(data: IrisData):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO iris_data (sepal_length, sepal_width )
            VALUES (%s, %s, %s, %s, %s)
        """, (
            data.sepal_length,
            data.sepal_width,
        ))
        conn.commit()
    return {"message": "Data inserted"}
