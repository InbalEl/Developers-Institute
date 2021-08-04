# change db

SELECT * FROM items ORDER BY price;

SELECT * FROM items WHERE price >= 80 ORDER BY price;

SELECT first_name, last_name FROM customers ORDER BY last_name LIMIT 3;

SELECT last_name FROM customers ORDER BY last_name DESC;

CREATE TABLE purchases(
    customer_id INTEGER REFERENCES customers(id),
    item_id INTEGER NOT NULL REFERENCES items(id)
);

INSERT INTO purchases(customer_id, item_id)
VALUES
    (1, 3),
    (4, 1),
    (5, 2),
    (3, 1),
    (2, 3);
    (6, 1);

SELECT * FROM purchases;

SELECT customers.first_name, customers.last_name, purchases.item_id FROM purchases INNER JOIN customers ON purchases.customer_id = customers.id;

SELECT customers.first_name, customers.last_name, purchases.item_id FROM purchases INNER JOIN customers ON purchases.customer_id = customers.id WHERE purchases.customer_id = 4;

SELECT customers.first_name, customers.last_name, purchases.item_id FROM purchases INNER JOIN customers ON purchases.customer_id = customers.id WHERE purchases.item_id = 1 OR purchases.item_id = 3;

SELECT
    customers.first_name,
    customers.last_name,
    items.name
FROM purchases
INNER JOIN customers ON purchases.customer_id = customers.id
INNER JOIN items ON purchases.item_id = items.id;
