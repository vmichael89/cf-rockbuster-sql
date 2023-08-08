queries = dict()

queries["FilmProfile"] = """

--Rockbuster Film Table Profile
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
FROM film"""

queries["CustomerProfile"] = """
--Rockbuster Customer Table Profile

SELECT
 'customer_id' AS column,
 SUM(CASE WHEN customer_id IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN customer_id IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT customer_id) AS 
duplicated,
 COUNT(DISTINCT customer_id) AS distinct,
STRING_AGG(DISTINCT customer_id::text, ', ') AS distinct_values
FROM customer
UNION ALL
SELECT
 'store_id' AS column,
 SUM(CASE WHEN store_id IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN store_id IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT store_id) AS duplicated,
 COUNT(DISTINCT store_id) AS distinct,
STRING_AGG(DISTINCT store_id::text, ', ') AS distinct_values
FROM customer
UNION ALL
SELECT
 'first_name' AS column,
 SUM(CASE WHEN first_name IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN first_name IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT first_name) AS 
duplicated,
 COUNT(DISTINCT first_name) AS distinct,
STRING_AGG(DISTINCT first_name::text, ', ') AS distinct_values
FROM customer
UNION ALL
SELECT
 'last_name' AS column,
 SUM(CASE WHEN last_name IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN last_name IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT last_name) AS duplicated,
 COUNT(DISTINCT last_name) AS distinct,
STRING_AGG(DISTINCT last_name::text, ', ') AS distinct_values
FROM customer
UNION ALL
SELECT
 'email' AS column,
 SUM(CASE WHEN email IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN email IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT email) AS duplicated,
 COUNT(DISTINCT email) AS distinct,
STRING_AGG(DISTINCT email::text, ', ') AS distinct_values
FROM customer
UNION ALL
SELECT
 'address_id' AS column,
 SUM(CASE WHEN address_id IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN address_id IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT address_id) AS 
duplicated,
 COUNT(DISTINCT address_id) AS distinct,
STRING_AGG(DISTINCT address_id::text, ', ') AS distinct_values
FROM customer
UNION ALL
SELECT
 'activebool' AS column,
 SUM(CASE WHEN activebool IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN activebool IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT activebool) AS 
duplicated,
 COUNT(DISTINCT activebool) AS distinct,
STRING_AGG(DISTINCT activebool::text, ', ') AS distinct_values
FROM customer
UNION ALL
SELECT
 'create_date' AS column,
 SUM(CASE WHEN create_date IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN create_date IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT create_date) AS 
duplicated,
 COUNT(DISTINCT create_date) AS distinct,
STRING_AGG(DISTINCT create_date::text, ', ') AS distinct_values
FROM customer
UNION ALL
SELECT
 'last_update' AS column,
 SUM(CASE WHEN last_update IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN last_update IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT last_update) AS 
duplicated,
 COUNT(DISTINCT last_update) AS distinct,
STRING_AGG(DISTINCT last_update::text, ', ') AS distinct_values
FROM customer
UNION ALL
SELECT
 'active' AS column,
 SUM(CASE WHEN active IS NULL THEN 1 ELSE 0 END) AS missing,
SUM(CASE WHEN active IS NOT NULL THEN 1 ELSE 0 END) - COUNT(DISTINCT active) AS duplicated,
 COUNT(DISTINCT active) AS distinct,
STRING_AGG(DISTINCT active::text, ', ') AS distinct_values
FROM customer"""

queries["FilmStats"] = """
--Rockbuster Film Table Statistics

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
FROM film"""

queries["CustomerStats"] = """
--Rockbuster Customer Table Statistics

SELECT
 'customer_id' AS column,
 MIN(customer_id),
 MAX(customer_id),
 AVG(customer_id),
 (SELECT MODE() WITHIN GROUP (ORDER BY customer_id))::VARCHAR,
 COUNT(customer_id),
 COUNT(*) AS count_rows
FROM customer
UNION ALL
SELECT
 'store_id' AS column,
 MIN(store_id),
 MAX(store_id),
 AVG(store_id),
 (SELECT MODE() WITHIN GROUP (ORDER BY store_id))::VARCHAR,
 COUNT(store_id),
 COUNT(*) AS count_rows
FROM customer
UNION ALL
SELECT
 'first_name' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY first_name))::VARCHAR,
 COUNT(first_name),
 COUNT(*) AS count_rows
FROM customer
UNION ALL
SELECT
 'last_name' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY last_name))::VARCHAR,
 COUNT(last_name),
 COUNT(*) AS count_rows
FROM customer
UNION ALL
SELECT
 'email' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY email))::VARCHAR,
 COUNT(email),
 COUNT(*) AS count_rows
FROM customer
UNION ALL
SELECT
 'address_id' AS column,
 MIN(address_id),
 MAX(address_id),
 AVG(address_id),
 (SELECT MODE() WITHIN GROUP (ORDER BY address_id))::VARCHAR,
 COUNT(address_id),
 COUNT(*) AS count_rows
FROM customer
UNION ALL
SELECT
 'activebool' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY activebool))::VARCHAR,
 COUNT(activebool),
 COUNT(*) AS count_rows
FROM customer
UNION ALL
SELECT
 'create_date' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY create_date))::VARCHAR,
 COUNT(create_date),
 COUNT(*) AS count_rows
FROM customer
UNION ALL
SELECT
 'last_update' AS column,
 NULL,
 NULL,
 NULL,
 (SELECT MODE() WITHIN GROUP (ORDER BY last_update))::VARCHAR,
 COUNT(last_update),
 COUNT(*) AS count_rows
FROM customer
UNION ALL
SELECT
 'active' AS column,
 MIN(active),
 MAX(active),
 AVG(active),
 (SELECT MODE() WITHIN GROUP (ORDER BY active))::VARCHAR,
 COUNT(active),
 COUNT(*) AS count_rows
FROM customer"""

queries["TopCountries"] = """
--Rockbuster Top 10 Countries Regarding Customers Count"

SELECT
D.country,
COUNT(customer_id) AS customer_count
FROM customer A
INNER JOIN address B ON A.address_id = B.address_id
INNER JOIN city C ON B.city_id = C.city_id
INNER JOIN country D ON C.country_ID = D.country_ID
GROUP BY country
ORDER BY customer_count DESC
LIMIT 10"""

queries["TopCities"] = """
--Rockbuster Top 10 Cities Regarding Customer Count within Top Countries

--CTE to get the top 10 countries regarding customer count
WITH top_countries AS (
 SELECT D.country
 FROM customer A
 INNER JOIN address B ON A.address_id = B.address_id
 INNER JOIN city C ON B.city_id = C.city_id
 INNER JOIN country D ON C.country_ID = D.country_ID
 GROUP BY D.country
 ORDER BY COUNT(*) DESC
 LIMIT 10)
--get the top 10 cities within the top countries
SELECT
 D.country,
 C.city,
 COUNT(*) AS customer_count_per_city
FROM customer A
INNER JOIN address B ON A.address_id = B.address_id
INNER JOIN city C ON B.city_id = C.city_id
INNER JOIN country D ON C.country_ID = D.country_ID
INNER JOIN top_countries ON D.country = top_countries.country --filter for top countries
GROUP BY D.country, city
ORDER BY customer_count_per_city DESC
LIMIT 10"""

queries["TopCustomers"] = """
--Rockbuster Top 5 Customers Regarding Total Payment within Top Cities

--subquery to get the top 10 countries regarding customer count
WITH top_countries AS (
 SELECT D.country
 FROM customer A
 INNER JOIN address B ON A.address_id = B.address_id
 INNER JOIN city C ON B.city_id = C.city_id
 INNER JOIN country D ON C.country_ID = D.country_ID
 GROUP BY D.country
 ORDER BY COUNT(*) DESC
 LIMIT 10
),
--get the top 10 cities within the top countries
top_cities_in_top_countries AS (
SELECT C.city
FROM customer A
INNER JOIN address B ON A.address_id = B.address_id
INNER JOIN city C ON B.city_id = C.city_id
INNER JOIN country D ON C.country_ID = D.country_ID
INNER JOIN top_countries E ON D.country = E.country --filter for top countries
GROUP BY D.country, C.city
ORDER BY COUNT(*) DESC
LIMIT 10
)
--from these cities
--get the top 5 customers with the highest total payments
SELECT
A.customer_id,
first_name,
last_name,
address,
C.city,
SUM(amount) AS total_payment
FROM customer A
INNER JOIN address B ON A.address_id = B.address_id
INNER JOIN city C ON B.city_id = C.city_id
INNER JOIN payment D ON D.customer_id = A.customer_id
INNER JOIN top_cities_in_top_countries E ON C.city = E.city
GROUP BY A.customer_id, first_name, last_name, address, C.city
ORDER BY total_payment DESC
LIMIT 5"""