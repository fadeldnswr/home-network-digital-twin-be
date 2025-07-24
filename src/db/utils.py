'''
Utilities for database operations in the home network digital twin project.
This module provides utility functions for interacting with the Supabase database.
'''
import os
import sys

from sqlmodel import Session, create_engine, select
from src.db.model import NetworkData
from src.exception.exception import CustomException
from typing import List

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USERNAME = os.getenv("DB_USERNAME")
SUPABASE_API_URL = os.getenv("SUPABASE_API_URL")

# Create session with SQLModel
db_url = f"postgresql://postgres:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_USERNAME}"
session_engine = create_engine(db_url, echo=True)

# Get all the network data logs from supabase using direct SQLModel queries
def get_all_network_logs() -> List[NetworkData]:
  try:
    with Session(session_engine) as session:
      statement = select(NetworkData)
      results = session.exec(statement)
      network = results.all()
      return network
  except Exception as e:
    raise CustomException(e, sys)