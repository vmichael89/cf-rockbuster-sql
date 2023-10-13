SQL Project: Rockbuster Stealth LLC - Movie Rental Company
===
![Rockbuster logo](images/logo.png "Rockbuster Logo")

Overview
---
This repository contains an in-depth SQL analysis of Rockbuster Stealth LLC, a former movie rental company that's transitioning to an online streaming platform. The analysis aims to provide data-driven insights to inform the company's strategic decisions as it faces competition from major streaming services.

Tools Used
---
- **SQL**: PostgreSQL 14, pgAdmin 4 v7.3
- **Python**:
  - pandas for data wrangling
  - googlemaps for geospatial data
  - psycopg2 for PostgreSQL interaction
  - sqlalchemy and graphviz for ERD generation
- **Tableau Public** v2023.2 for visualization
- **Powerpoint** for reporting

Special Challenges
---
- Many city locations were not recognized by Tableau. I used the `restcountries` API in combination with `googlemaps` API to get the location data for for all cities.
- Leveraged `psycopg2` library to interact with the database via Python. That way I could automate
  - the documentation of SQL queries to Excel
  - the generation of an ERD using `sqlalchemy` and `graphviz`
  - the generation of long SQL queries

Links
---
[Powerpoint Report](report/Final%20Presentation.pdf)

[Tableau Repository](https://public.tableau.com/authoring/CareerFoundry_DataAnalytics_3_10_PresentingSQLResults/RevenueRentalCountRate#1)

Objective
---

Rockbuster expects data-driven answers they can use for their company strategy addressing the follwing key business question:

- Which movies contributed the most/least to revenue gain?
- What was the average rental duration for all videos?
- Which countries are Rockbuster customers based in?
- Where are customers with a high lifetime value based?
- Do sales figures vary between geographic regions?

Project Structure
---

    ├── README.md
    │
    ├── data
    │   ├── dvdrental.tar               # SQL database
    │   ├── film_stock_course.xlsx      #
    │   └── countries_geo.xlsx          # 
    │
    ├── images                          # images for the readme
    │
    ├── input                           # Task project brief
    │
    ├── report
    │   ├── Final Presentation.pdf      
    │   └── SQL_Queries.xlsx            # query results from ./scripts/sql
    │
    ├── requirements.txt                
    │
    └── scripts
        ├── python
        │   ├── entity_relationship_diagram
        │   │   ├── Rockbuster_ERD
        │   │   ├── Rockbuster_ERD.png
        │   │   ├── sql_db_to_models.py
        │   │   ├── sql_models.py
        │   │   └── sql_models_to_erd.py
        │   ├── 01_store_sql_query_results.py       # -> SQL_Queries.xlsx
        │   ├── 02_calc_stock_count_over_time.py    # -> film_stock_course.xlsx
        │   ├── 03_clean_geospatial_data.py         # -> countries_geo.xslx
        │   ├── queries.py                          # collection of queries
        │   └── sql_helper.py                       # database interaction and query builder
        │
        └── sql
            ├── customer_table_profiling.sql
            ├── customer_table_statistics.sql
            ├── film_table_profiling.sql
            ├── film_table_statistics.sql
            ├── top_customers_cte.sql
            └── top_customers_subquery.sql

Installation
---

To execute the Python scripts, please consult `scripts/python/requirements.txt` for the required dependencies.

A PostgresSQL Database must be installed with the following credentials:
``` 
"host": "localhost",
"port": 5432,
"database": "Rockbuster",
"user": "postgres",
"password": "1234"
```
The database file is located at `data/dvdrentals.tar`. It can be imported with pgAdmin.

Data Set
---

`.data / dvdrental.tar`

Provider: https://www.postgresqltutorial.com/

Data set that contains information about Rockbuster’s film inventory, customers, and payments, among other things. See complete ERD below. The data set has 14,596 records of movie rentals from 599 customers in different cities and countries. 

![Entity relationship diagram](./images/dvdrental_erd.png "Entity Relationship Diagram")
ERD generated with `sqlalchemy` and `graphviz`

<br>

`.data / film_stock_course.xlsx`

Wrangled data showing rentals over time.

<br>

`.data / countries_geo.xlsx`

Curated city and country data with added latitude, longitude and regions to city data using googlemaps api and restcountries


Most Intersting Finding
---

Upon delving into the data, I discovered that Rockbuster imposes a **$1 daily fee** for overdue rentals. Interestingly, these overdue charges contribute to **30% of the total revenue** due to short loan periods. This could raise ethical issues. Customers might argue that Rockbuster Stealth LLC intentionally sets shorter loan periods as a strategy to boost their revenue.

![Overdue fees](images/report_excerpt_fees.png)

For the detailed in-depth analysis refer to the [complete report](report/Final%20Presentation.pdf).
