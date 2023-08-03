-- Rockbuster Customer Table Statistics

-- creates an overview with
--  column names
-- 	minimum values
--	maximum values
--	mean values
--  mode (type casted to string to allow multiple data types)
--  number of rows

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
FROM customer
