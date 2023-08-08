from sqlalchemy import create_engine, MetaData
from sqlacodegen.codegen import CodeGenerator

# Connection properties
props = {
    "host": "localhost",
    "port": 5432,
    "database": "Rockbuster",
    "user": "postgres",
    "password": "1234"
}

# Connect to the PostgresSQL database
conn_string = f"postgresql://{props['user']}:{props['password']}@{props['host']}:{props['port']}/{props['database']}"
engine = create_engine(conn_string)
conn = engine.connect()

# Generate SQLAlchemy models from the database
metadata = MetaData(bind=engine)
metadata.reflect()

generator = CodeGenerator(metadata)

# Redirect the standard output to a file
with open("sql_models.py", "w") as f:
    generator.render(f)

# Close the database connection
conn.close()
