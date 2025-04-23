CREATE TABLE IF NOT EXISTS iris_data (
    id SERIAL PRIMARY KEY,
    sepal_length FLOAT,
    sepal_width FLOAT,
    petal_length FLOAT,
    petal_width FLOAT,
    species VARCHAR(50)
);
