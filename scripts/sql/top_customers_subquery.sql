-- Get the average payment
-- of the 5 top paying customers
-- within the top 10 grossing cities 
-- within the top 10 grossing countries
-- using a subquery

--get the average total amount paid by the top 5 customers
SELECT
AVG(total_amount_paid.total_payment)
FROM
(--subquery to get the top 10 countries regarding customer count
WITH
top_countries AS (
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
LIMIT 5) AS total_amount_paid