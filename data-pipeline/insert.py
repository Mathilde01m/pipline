import pandas as pd
import psycopg2

# Lecture du CSV
df = pd.read_csv("iris 1.csv")

# Connexion à PostgreSQL
conn = psycopg2.connect(
    dbname="irisdb",
    user="irisuser",
    password="irispass",
    host="localhost",
    port="5432"
)

# Insertion dans la table iris_data
with conn:
    with conn.cursor() as cur:
        for _, row in df.iterrows():
            cur.execute("""
                INSERT INTO iris_data (sepal_length, sepal_width)
                VALUES (%s, %s)
            """, (row["sepal_length"], row["sepal_width"]))
print(f"✅ {len(df)} lignes insérées dans la table iris_data.")

conn.close()
