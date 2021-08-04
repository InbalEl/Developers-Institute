SELECT * FROM customer;

SELECT CONCAT(first_name, ' ' ,last_name) AS "Full Name" FROM customer;

SELECT DISTINCT create_date FROM customer;

SELECT * FROM customer ORDER BY first_name DESC;

SELECT
    film_id,
    title,
    description,
    release_year,
    rental_rate
FROM film
ORDER BY rental_rate;

SELECT address, address2, phone FROM address WHERE district = 'Texas';

SELECT * FROM film WHERE film_id BETWEEN 15 AND 150;

SELECT
    film_id,
    title,
    description,
    length,
    rental_rate
FROM film
WHERE title ILIKE 'My%';

SELECT title, rental_rate FROM film ORDER BY rental_rate LIMIT 10;
SELECT title, rental_rate FROM film ORDER BY rental_rate OFFSET 10 LIMIT 10;
SELECT title, rental_rate FROM film ORDER BY rental_rate OFFSET 10 FETCH FIRST 10 ROWS ONLY;

SELECT
    payment.amount,
    payment.payment_date,
    customer.first_name,
    customer.last_name
FROM customer
INNER JOIN payment ON customer.customer_id = payment.customer_id
ORDER BY customer.customer_id;

SELECT
    film.title,
    inventory.inventory_id
FROM inventory
INNER JOIN film ON inventory.film_id = film.film_id
ORDER BY inventory.film_id;

SELECT
    film.title
FROM
    film
INNER JOIN inventory ON film.film_id = inventory.film_id
WHERE film.film_id NOT IN (SELECT film_id FROM inventory);

SELECT DISTINCT
    city.city,
    country.country
FROM
    city
INNER JOIN country ON city.country_id = country.country_id
ORDER BY country.country;

SELECT
    customer.customer_id,
    CONCAT(customer.first_name, ' ', customer.last_name) AS "Customer Name",
    payment.amount,
    payment.payment_date,
    CONCAT(staff.first_name, ' ', staff.last_name) AS "Staff Name",
    staff.staff_id
FROM customer
INNER JOIN payment ON customer.customer_id = payment.customer_id
INNER JOIN staff ON payment.staff_id = staff.staff_id
ORDER BY staff.staff_id;