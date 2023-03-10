CREATE TABLE edificacao (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    geom geometry(POLYGON,4674)
);