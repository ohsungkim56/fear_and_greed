import os
from sqlalchemy import create_engine

DB_PORT = os.getenv("DB_PORT", "NO POSTGRES PORT SET")
DB_HOST = os.getenv("DB_HOST", "NO POSTGRES HOST SET")
DB_USER = os.getenv("DB_USER", "NO POSTGRES USER SET")
DB_PASSWORD = os.getenv("DB_PASSWORD", "NO POSTGRES PASSWORD SET")

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres", echo=False)
