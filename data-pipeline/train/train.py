from sqlalchemy import create_engine
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn
import joblib

# Connexion PostgreSQL
engine = create_engine("postgresql+psycopg2://irisuser:irispass@db:5432/irisdb")
df = pd.read_sql("SELECT sepal_length, sepal_width FROM iris_data", engine)

print("📊 Données chargées :", df.shape[0], "lignes")

if df.empty:
    raise ValueError("❌ La table iris_data est vide. Veuillez insérer les données d'entraînement.")

X = df[["sepal_width"]]
y = df["sepal_length"]

model = RandomForestRegressor(random_state=42)
model.fit(X, y)
preds = model.predict(X)
mse = mean_squared_error(y, preds)

mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("iris-regression")

with mlflow.start_run() as run:
    mlflow.log_param("model_type", "RandomForestRegressor")
    mlflow.log_metric("mse", mse)
    mlflow.sklearn.log_model(model, artifact_path="model")
    joblib.dump(model, "iris_model.pkl")
    print(f"🔁 Run ID pour chargement MLflow : {run.info.run_id}")

print(f"✅ Modèle entraîné avec MSE={mse:.4f} et sauvegardé dans MLflow + .pkl")