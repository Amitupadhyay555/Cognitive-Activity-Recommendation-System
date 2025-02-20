# from sqlalchemy import create_engine, Column, Integer, String, Index
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import os
# from backend.config import DATABASE_URL  # Keep this import, as you're using DATABASE_URL from config

# # Check if the DATABASE_URL environment variable is set, otherwise fall back to the local URL.
# DATABASE_URL = os.environ.get('DATABASE_URL', DATABASE_URL)

# # Create the engine
# engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)  # Optional improvement for scalability
# Base = declarative_base()

# # Define your Activity model as before
# class Activity(Base):
#     __tablename__ = "activities"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String, nullable=False)
#     description = Column(String, nullable=False)
#     zone = Column(String, nullable=False)
#     time_required = Column(Integer, nullable=False)
#     age_range = Column(String, nullable=False)
#     category = Column(String, nullable=False)

#     # Adding indexes for optimization
#     Index('ix_activity_category', 'category')
#     Index('ix_activity_zone', 'zone')
#     Index('ix_activity_age_range', 'age_range')

# # Create tables (Make sure this runs before inserting data)
# Base.metadata.create_all(engine)

# # Session Factory
# SessionLocal = sessionmaker(bind=engine)

# def get_session():
#     return SessionLocal()

# DEBUG = True




from sqlalchemy import create_engine, Column, Integer, String, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from backend.config import DATABASE_URL  # Keep this import, as you're using DATABASE_URL from config

# Ensure DATABASE_URL is correctly set in the environment (or fall back to local if running locally)
DATABASE_URL = os.environ.get('DATABASE_URL', DATABASE_URL)

# Create the engine
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

Base = declarative_base()

# Define the Activity model as before
class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    zone = Column(String, nullable=False)
    time_required = Column(Integer, nullable=False)
    age_range = Column(String, nullable=False)
    category = Column(String, nullable=False)

    # Add indexes for optimization
    Index('ix_activity_category', 'category')
    Index('ix_activity_zone', 'zone')
    Index('ix_activity_age_range', 'age_range')

# Create tables (Make sure this runs before inserting data)
Base.metadata.create_all(engine)

# Session Factory
SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()

