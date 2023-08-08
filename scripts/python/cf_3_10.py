from pathlib import Path

import pandas as pd

from sql_helper import Database
from queries import queries


output_file = "SQL_Queries.xlsx"

db = Database()

with pd.ExcelWriter(output_file) as writer:
    for i, (title, query) in enumerate(queries.items()):
        # run query on database
        res_df = db.query(query)

        # Split query into lines to avoid need cell formatting in Excel
        qry_df = pd.DataFrame({title: query.strip('\n').split('\n')})

        # Write output and query to Excel on separate sheets
        res_df.to_excel(writer, sheet_name=title, index=False)
        qry_df.to_excel(writer, sheet_name=f'Q{i + 1:02}', index=False)

queries = []

query = """--film inventory counts
SELECT
    title,
    COUNT(*) AS inventory_count
FROM film
INNER JOIN inventory ON inventory.film_id = film.film_id
GROUP BY title
ORDER BY inventory_count DESC"""
inventory_counts = db.query(query)
queries.append(query)

query = """--rental course
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
"""
rentals = db.query(query)
queries.append(query)

rentals["delta_stock"] = rentals.groupby("title")["delta"].transform("cumsum")

rent_inv = rentals.merge(inventory_counts)
rent_inv["stock"] = rent_inv["inventory_count"] + rent_inv["delta_stock"]

rent_inv.to_excel("film_stock_course.xlsx")