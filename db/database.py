from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# TODO: Implement all of these..
SQLALCHEMY_DB_URL = "sqlite:////users.db"

engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})
# connect_args is only for SQLite


Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
