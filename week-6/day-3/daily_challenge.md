CREATE DATABASE martiandb

#\c martiandb

CREATE TABLE base(
    id SERIAL PRIMARY KEY,
    base_name VARCHAR(20)
)

CREATE TABLE martian(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    base_id INTEGER REFERENCES base(id),
    super_id INTEGER,
    CONSTRAINT fk_super FOREIGN KEY (super_id) REFERENCES martian(id)
);

CREATE TABLE visitor(
    visitor_id SERIAL PRIMARY KEY,
    host_id INTEGER REFERENCES martian(id),
    first_name VARCHAR(20),
    last_name VARCHAR(20)
)


INSERT INTO base(base_name)
VALUES('Tharsisland'),
      ('Gale Cratertown'),
      ('New New New York'),
      ('Valles Marineris 2.0');

INSERT INTO martian(first_name, last_name, base_id)
VALUES
('Ray', 'Bradbury', 1),
('John', 'Snow', 2),
('Samuel', 'Hinkston', 1),
('Hank', 'Green', 3),
('John', 'Green', 2),
('Elma', 'Parkhill', 4),
('Melisaa', 'McCall', 2),
('Chris', 'Argent', 3),
('Elon', 'Musk', 4);

UPDATE martian
SET super_id = 3
WHERE last_name = 'Green';

UPDATE martian
SET super_id = 4
WHERE base_id = 1;

UPDATE martian
SET super_id = 2
WHERE base_id = 2;

UPDATE martian
SET super_id = 4
WHERE super_id  is null;

INSERT INTO visitor(host_id, first_name, last_name)
VALUES
(6, 'Jamie', 'Waterman'),
(1, 'Jane', 'Thornton'),
(3, 'Kris', 'Cardenas');

SELECT
    v.first_Name AS visitor_fn,
    v.last_Name AS visitor_ln,
    m.first_Name AS host_fn,
    m.last_Name AS host_ln
FROM visitor AS v
INNER JOIN martian as m
ON m.id = v.host_id;

SELECT
    v.first_Name AS visitor_fn,
    v.last_Name AS visitor_ln,
    m.first_Name AS host_fn,
    m.last_Name AS host_ln
FROM visitor AS v
LEFT OUTER JOIN martian as m
ON m.id = v.host_id;

SELECT
    v.first_Name AS visitor_fn,
    v.last_Name AS visitor_ln,
    m.first_Name AS host_fn,
    m.last_Name AS host_ln
FROM visitor AS v
RIGHT OUTER JOIN martian as m
ON m.id = v.host_id;

SELECT
    v.first_Name AS visitor_fn,
    v.last_Name AS visitor_ln,
    m.first_Name AS host_fn,
    m.last_Name AS host_ln
FROM visitor AS v
FULL OUTER JOIN martian as m
ON m.id = v.host_id;