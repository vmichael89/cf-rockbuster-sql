import pandas as pd

from sql_helper import Database
from queries import queries  # loads the variable queries (list of strings) from queries.py

# Excel file to store sql queries with results
output_file = "../../report/SQL_Queries.xlsx"

# Connect to Rockbuster sql database
db = Database()

# run queries from queries.py and store results in an Excel file
with pd.ExcelWriter(output_file) as writer:
    for i, (title, query) in enumerate(queries.items()):
        # Run query on database
        res_df = db.query(query)

        # Split query into lines to avoid need cell formatting in Excel
        qry_df = pd.DataFrame({title: query.strip('\n').split('\n')})

        # Write output and query to Excel on separate sheets
        res_df.to_excel(writer, sheet_name=title, index=False)
        qry_df.to_excel(writer, sheet_name=f'Q{i + 1:02}', index=False)
