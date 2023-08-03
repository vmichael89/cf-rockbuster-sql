-- Rockbuster Customer Table Profile

-- creates an overview with
-- 	column names
-- 	number of missing values
--	number of duplicated values
--	list of distinct values

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
FROM customer