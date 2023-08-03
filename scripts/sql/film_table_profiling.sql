-- Rockbuster Film Table Profile

-- creates an overview with
-- 	column names
-- 	number of missing values
--	number of duplicated values
--	list of distinct values

SELECT
 'film_id' AS column,
 SUM(CASE WHEN film_id IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN film_id IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT film_id) AS duplicated,
 COUNT(DISTINCT film_id) AS distinct,
STRING_AGG(DISTINCT film_id::text, ', ') AS distinct_values
FROM film
UNION ALL
SELECT
 'title' AS column,
 SUM(CASE WHEN title IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN title IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT title) AS duplicated,
 COUNT(DISTINCT title) AS distinct,
STRING_AGG(DISTINCT title::text, ', ') AS distinct_values
FROM film
UNION ALL
SELECT
 'description' AS column,
 SUM(CASE WHEN description IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN description IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT description) AS 
duplicated,
 COUNT(DISTINCT description) AS distinct,
STRING_AGG(DISTINCT description::text, ', ') AS distinct_values
FROM film
UNION ALL
SELECT
 'release_year' AS column,
 SUM(CASE WHEN release_year IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN release_year IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT release_year) AS 
duplicated,
 COUNT(DISTINCT release_year) AS distinct,
STRING_AGG(DISTINCT release_year::text, ', ') AS distinct_values
FROM film
UNION ALL
SELECT
 'language_id' AS column,
 SUM(CASE WHEN language_id IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN language_id IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT language_id) AS 
duplicated,
 COUNT(DISTINCT language_id) AS distinct,
STRING_AGG(DISTINCT language_id::text, ', ') AS distinct_values
FROM film
UNION ALL
SELECT
 'rental_duration' AS column,
 SUM(CASE WHEN rental_duration IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN rental_duration IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT rental_duration) AS 
duplicated,
 COUNT(DISTINCT rental_duration) AS distinct,
STRING_AGG(DISTINCT rental_duration::text, ', ') AS distinct_values
FROM film
UNION ALL
SELECT
 'rental_rate' AS column,
 SUM(CASE WHEN rental_rate IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN rental_rate IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT rental_rate) AS 
duplicated,
 COUNT(DISTINCT rental_rate) AS distinct,
STRING_AGG(DISTINCT rental_rate::text, ', ') AS distinct_values
FROM film
UNION ALL
SELECT
 'length' AS column,
 SUM(CASE WHEN length IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN length IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT length) AS duplicated,
 COUNT(DISTINCT length) AS distinct,
STRING_AGG(DISTINCT length::text, ', ') AS distinct_values
FROM film
UNION ALL
SELECT
 'replacement_cost' AS column,
 SUM(CASE WHEN replacement_cost IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN replacement_cost IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT replacement_cost) 
AS duplicated,
 COUNT(DISTINCT replacement_cost) AS distinct,
STRING_AGG(DISTINCT replacement_cost::text, ', ') AS distinct_values
FROM film
UNION ALL
SELECT
 'rating' AS column,
 SUM(CASE WHEN rating IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN rating IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT rating) AS duplicated,
 COUNT(DISTINCT rating) AS distinct,
STRING_AGG(DISTINCT rating::text, ', ') AS distinct_values
FROM film
UNION ALL
SELECT
 'last_update' AS column,
 SUM(CASE WHEN last_update IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN last_update IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT last_update) AS 
duplicated,
 COUNT(DISTINCT last_update) AS distinct,
STRING_AGG(DISTINCT last_update::text, ', ') AS distinct_values
FROM film
UNION ALL
SELECT
 'special_features' AS column,
 SUM(CASE WHEN special_features IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN special_features IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT special_features) 
AS duplicated,
 COUNT(DISTINCT special_features) AS distinct,
STRING_AGG(DISTINCT special_features::text, ', ') AS distinct_values
FROM film
UNION ALL
SELECT
 'fulltext' AS column,
 SUM(CASE WHEN fulltext IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN fulltext IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT fulltext) AS duplicated,
 COUNT(DISTINCT fulltext) AS distinct,
STRING_AGG(DISTINCT fulltext::text, ', ') AS distinct_values
FROM film
