import pandas as pd
import requests

df = pd.read_csv("iris 1.csv")
data = df.head(2).to_dict(orient="records")

for row in data:
    response = requests.post("http://localhost:8000/insert", json=row)
    print(response.status_code, response.json())
