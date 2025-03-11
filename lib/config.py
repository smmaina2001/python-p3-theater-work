from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///moringa_theater.db"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()

# Create a session instance
session = Session()  