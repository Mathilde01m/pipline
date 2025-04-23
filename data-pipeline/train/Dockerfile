FROM python:3.10

WORKDIR /app
COPY ../train.py .
RUN pip install pandas scikit-learn psycopg2-binary mlflow

CMD ["python", "train.py"]
