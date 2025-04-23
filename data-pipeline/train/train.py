import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Chargement du CSV
df = pd.read_csv("../iris 1.csv")

# Nettoyage des noms de colonnes (important si tu as des espaces ou majuscules)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Préparation des données
X = df[['sepal_width']]
y = df['sepal_length']

# Entraînement
model = RandomForestRegressor()
model.fit(X, y)

# Évaluation
mse = mean_squared_error(y, model.predict(X))
print(f"✅ Modèle entraîné — MSE : {mse:.2f}")

# Sauvegarde du modèle
joblib.dump(model, "../app/iris_model.pkl")
print("✅ Modèle sauvegardé dans ../app/iris_model.pkl")
