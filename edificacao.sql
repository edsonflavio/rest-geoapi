CREATE TABLE edificacao (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    geom geometry(POLYGON,4674)
);
