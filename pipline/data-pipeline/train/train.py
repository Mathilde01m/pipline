import pandas as pd
import psycopg2
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn

# Connexion à PostgreSQL
conn = psycopg2.connect(
    dbname="irisdb",
    user="irisuser",
    password="irispass",
    host="db",     # c'est le nom du service dans docker-compose
    port="5432"
)

# Chargement des données
query = "SELECT sepal_length, sepal_width FROM iris_data"
df = pd.read_sql(query, conn)

X = df[['sepal_width']]
y = df['sepal_length']

# Entraînement du modèle
model = RandomForestRegressor()
model.fit(X, y)
preds = model.predict(X)
mse = mean_squared_error(y, preds)

# Suivi avec MLflow
mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("iris-regression")

with mlflow.start_run():
    mlflow.log_param("model_type", "RandomForestRegressor")
    mlflow.log_metric("mse", mse)
    mlflow.sklearn.log_model(model, "model")

print("Modèle entraîné et loggé dans MLflow ✅")
