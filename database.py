from password_file import PASSWORD
from sqlalchemy import create_engine
import psycopg2

engine = create_engine(
    f"postgresql+psycopg2://umut:{PASSWORD}@localhost:5432/ProductList",
    echo=True
)


conn = engine.connect()
conn.execute("SELECT * FROM prodcuts")
