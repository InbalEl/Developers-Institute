CREATE DATABASE public;

# change db?

CREATE TABLE items(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price SMALLINT NOT NULL
);

CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

INSERT INTO items(name, price)
values
    ('Small Desk', 100),
    ('Large Desk', 300),
    ('Fan', 80);

INSERT INTO customers(first_name, last_name)
values
    ('Stiles', 'Stilinski'),
    ('Scott', 'McCall'),
    ('Derek', 'Hale'),
    ('Peter', 'Hale'),
    ('Lydia', 'Martin'),
    ('Chris', 'Argent');

SELECT * FROM items;
SELECT * FROM items WHERE price > 80;
SELECT * FROM items WHERE price <= 300;

SELECT * FROM customers WHERE last_name = 'Smith';
SELECT * FROM customers WHERE last_name = 'Hale';
SELECT * FROM customers WHERE last_name != 'McCall';