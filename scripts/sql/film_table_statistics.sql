-- Rockbuster Film Table Statistics

-- creates an overview with
--  column names
-- 	minimum values
--	maximum values
--	mean values
--  mode (type casted to string to allow multiple data types)
--  number of rows

SELECT
 'film_id' AS column,
 MIN(film_id),
 MAX(film_id),
 AVG(film_id),
 (SELECT MODE() WITHIN GROUP (ORDER BY film_id))::VARCHAR,
 COUNT(film_id),
 COUNT(*) AS count_rows
FROM film
UNION ALL
SELECT
 'title' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY title))::VARCHAR,
 COUNT(title),
 COUNT(*) AS count_rows
FROM film
UNION ALL
SELECT
 'description' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY description))::VARCHAR,
 COUNT(description),
 COUNT(*) AS count_rows
FROM film
UNION ALL
SELECT
 'release_year' AS column,
 MIN(release_year),
 MAX(release_year),
 AVG(release_year),
 (SELECT MODE() WITHIN GROUP (ORDER BY release_year))::VARCHAR,
 COUNT(release_year),
 COUNT(*) AS count_rows
FROM film
UNION ALL
SELECT
 'language_id' AS column,
 MIN(language_id),
 MAX(language_id),
 AVG(language_id),
 (SELECT MODE() WITHIN GROUP (ORDER BY language_id))::VARCHAR,
 COUNT(language_id),
 COUNT(*) AS count_rows
FROM film
UNION ALL
SELECT
 'rental_duration' AS column,
 MIN(rental_duration),
 MAX(rental_duration),
 AVG(rental_duration),
 (SELECT MODE() WITHIN GROUP (ORDER BY rental_duration))::VARCHAR,
 COUNT(rental_duration),
 COUNT(*) AS count_rows
FROM film
UNION ALL
SELECT
 'rental_rate' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY rental_rate))::VARCHAR,
 COUNT(rental_rate),
 COUNT(*) AS count_rows
FROM film
UNION ALL
SELECT
 'length' AS column,
 MIN(length),
 MAX(length),
 AVG(length),
 (SELECT MODE() WITHIN GROUP (ORDER BY length))::VARCHAR,
 COUNT(length),
 COUNT(*) AS count_rows
FROM film
UNION ALL
SELECT
 'replacement_cost' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY replacement_cost))::VARCHAR,
 COUNT(replacement_cost),
 COUNT(*) AS count_rows
FROM film
UNION ALL
SELECT
 'rating' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY rating))::VARCHAR,
 COUNT(rating),
 COUNT(*) AS count_rows
FROM film
UNION ALL
SELECT
 'last_update' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY last_update))::VARCHAR,
 COUNT(last_update),
 COUNT(*) AS count_rows
FROM film
UNION ALL
SELECT
 'special_features' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY special_features))::VARCHAR,
 COUNT(special_features),
 COUNT(*) AS count_rows
FROM film
UNION ALL
SELECT
 'fulltext' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY fulltext))::VARCHAR,
 COUNT(fulltext),
 COUNT(*) AS count_rows
FROM film

