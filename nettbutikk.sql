USE nettbutikk;


CREATE TABLE users (
    id          INTEGER PRIMARY KEY AUTO_INCREMENT,
    username    VARCHAR(50)    NOT NULL UNIQUE,
    passord     VARCHAR(50)    NOT NULL
);


CREATE TABLE produkt (
    id          INTEGER PRIMARY KEY AUTO_INCREMENT,
    kapittel     VARCHAR(100)    NOT NULL,
    price       REAL            NOT NULL,
    name        VARCHAR(50)    NOT NULL
);


