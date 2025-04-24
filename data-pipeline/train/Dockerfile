FROM python:3.11-slim

WORKDIR /app

COPY train.py .

RUN pip install pandas scikit-learn sqlalchemy psycopg2-binary mlflow joblib

CMD ["python", "train.py"]