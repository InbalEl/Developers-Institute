SELECT first_name, last_name, birth_date FROM students order by last_name limit 4;

SELECT first_name, last_name, birth_date FROM students order by birth_date desc limit 1;

SELECT first_name, last_name, birth_date FROM students order by last_name offset 2 limit 3;