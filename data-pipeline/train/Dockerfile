FROM python:3.11-slim

WORKDIR /app

COPY train.py .

RUN pip install pandas scikit-learn sqlalchemy psycopg2-binary mlflow

CMD ["python", "train.py"]