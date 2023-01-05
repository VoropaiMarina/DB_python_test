CREATE USER postgres WITH LOGIN PASSWORD '1111';
CREATE DATABASE pg_db;
GRANT ALL PRIVILEGES ON DATABASE pg_db TO postgres;
CREATE TABLE test(
    ID                 SERIAL,
    TS                    DATE    NOT NULL,
    NUMBER             INTEGER   NOT NULL
);