SELECT f.title, l.name
FROM film as f
INNER JOIN language as l
ON f.language_id = l.language_id;


SELECT f.title, f.description, l.name
FROM film as f
INNER JOIN language as l
ON f.language_id = l.language_id;


SELECT f.title, f.description, l.name
FROM film as f
LEFT OUTER JOIN language as l
ON f.language_id = l.language_id;


SELECT f.title, f.description, l.name
FROM film as f
RIGHT OUTER JOIN language as l
ON f.language_id = l.language_id;


CREATE TABLE new_film(
    id SERIAL PRIMARY KEY,
    name varchar(50)
);


INSERT INTO new_film(name)
VALUES ('How To Train Your Dragon'),
    ('How To Train Your Dragon 2'),
    ('Serenity');


CREATE TABLE customer_review(
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INTEGER REFERENCES language(language_id),
    title VARCHAR(50),
    score SMALLINT,
    review_text TEXT,
    last_update DATE,
    CHECK (score BETWEEN 1 AND 10)
);

INSERT INTO customer_review(film_id, language_id, title, score, review_text)
VALUES(
    1, 1, 'Training Dragons', 10, 'Best movie ever'
),
(
    2, 1, 'Return of Toothless', 10, 'Nope, this one is better than the first'
),
(
    3, 1, 'Space Westerns', 7, 'A poor excuse of what should have been a glorious tv series with many more seasons. Will never forgive Firefly being canceled.'
);


SELECT * FROM new_film;
SELECT * FROM customer_review;
DELETE FROM new_film WHERE id=2;
SELECT * FROM new_film;
SELECT * FROM customer_review;

UPDATE film
SET language_id = 2
WHERE film_id BETWEEN 150 AND 170;

# Foreign-key constraints:
#   "customer_address_id_fkey" FOREIGN KEY (address_id) REFERENCES
#   address(address_id) ON UPDATE CASCADE ON DELETE RESTRICT

# I think it means an address must be inserted into the address table before we can insert a new customer

DROP TABLE customer_review;

# did not require any other action

SELECT return_date from rental;

SELECT * from rental WHERE return_date > now();


SELECT f.title, f.rental_rate
FROM film AS f
INNER JOIN inventory AS i ON i.film_id = f.film_id
INNER JOIN (SELECT * from rental) AS rentals
ON rentals.inventory_id = i.inventory_id
ORDER BY f.rental_rate DESC LIMIT 30;


SELECT f.title, f.rental_rate
FROM film AS f
INNER JOIN inventory AS i ON i.film_id = f.film_id
INNER JOIN (SELECT * from rental WHERE return_date > now()) AS rentals
ON rentals.inventory_id = i.inventory_id
ORDER BY f.rental_rate DESC LIMIT 30;

SELECT f.title FROM film AS f
INNER JOIN
    (SELECT * FROM film_actor as fa
    INNER JOIN
        (SELECT * FROM actor AS a
        WHERE a.first_name ILIKE 'Penelope' AND a.last_name ILIKE 'Monroe')
        AS pm
    ON pm.actor_id=fa.actor_id)
    AS pm_movies
ON pm_movies.film_id=f.film_id
WHERE f.description ILIKE '%sumo%';


SELECT f.title, f.length, f.rating
FROM film as f
INNER JOIN (
    SELECT category_id,film_id FROM film_category WHERE (SELECT name from category where category_id=) ILIKE '%documentary%'
) as fc
ON fc.film_id=f.film_id
WHERE f.length < 60 AND f.rating ILIKE 'R';


CREATE VIEW film_id_categories AS
SELECT c.name, fc.film_id FROM category AS c
INNER JOIN film_category AS fc
ON fc.category_id=c.category_id

SELECT f.title, fid.name, f.length FROM film_id_categories AS fid
INNER JOIN film as f
ON f.film_id=fid.film_id
WHERE f.rating = 'R' AND f.length < 60 and fid.name ILIKE 'documentary';


CREATE VIEW inventory_rate AS
SELECT i.inventory_id, f.film_id, f.rental_rate from film as f
INNER JOIN inventory as i
ON f.film_id = i.film_id;


SELECT ir.rental_rate, r.return_date, c.first_name, c.last_name
FROM rental as r
INNER JOIN customer AS c
ON r.customer_id = c.customer_id
INNER JOIN inventory_rate AS ir
ON ir.inventory_id = r.inventory_id
WHERE
    c.first_name ILIKE 'matthew' AND
    c.last_name ILIKE 'mahan' AND
    '2005-07-28' <= r.return_date AND r.return_date <= '2005-08-01' AND
    ir.rental_rate > 4;


SELECT DISTINCT f.title, f.rental_rate from film as f
INNER JOIN rental AS r
ON r.customer_id = (SELECT customer_id FROM customer WHERE first_name ILIKE 'matthew' AND last_name ILIKE 'mahan')
WHERE f.title ILIKE '%boat%' OR f.description ILIKE '%boat%'
ORDER BY f.rental_rate DESC;

