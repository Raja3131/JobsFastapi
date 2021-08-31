import databases, sqlalchemy

# Postgres Database
DATABASE_URL = "postgresql://postgres:313131@127.0.0.1:5432/api"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

jobs = sqlalchemy.Table(
    "py_users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("create_at", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)
