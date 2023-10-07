from sql_helper import Database

# Connect to Rockbuster sql database
db = Database()

# get inventory counts by grouping inventory by title
inventory_counts = db.query(
"""--film inventory counts
SELECT
    title,
    COUNT(*) AS inventory_count
FROM film
INNER JOIN inventory ON inventory.film_id = film.film_id
GROUP BY title
ORDER BY inventory_count DESC""")

# query title, return/rental date with flag if film was returned (1) or rented (-1)
# flatten return and rental dates using 2 queries and UNION
rentals = db.query(
"""--rental course
SELECT
	title,
	rental_date AS date,
	-1 AS delta
FROM film A
INNER JOIN inventory B ON A.film_id=B.film_id
INNER JOIN rental C ON B.inventory_id=C.inventory_id
UNION ALL
SELECT
	title,
	return_date AS date,
	1 AS delta
FROM film A
INNER JOIN inventory B ON A.film_id=B.film_id
INNER JOIN rental C ON B.inventory_id=C.inventory_id
ORDER BY date
""")

# calculate how many films are currently rented
rentals["delta_stock"] = rentals.groupby("title")["delta"].transform("cumsum")

rent_inv = rentals.merge(inventory_counts)  # automatically merges on 'title'

# calculate stock count
rent_inv["stock"] = rent_inv["inventory_count"] + rent_inv["delta_stock"]

# save data
rent_inv.to_excel("film_stock_course.xlsx")