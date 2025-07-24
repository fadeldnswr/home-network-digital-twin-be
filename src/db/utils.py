'''
Utilities for database operations in the home network digital twin project.
This module provides utility functions for interacting with the Supabase database.
'''
import os
import sys

from sqlmodel import Session, create_engine
from db.model import NetworkLogs
from src.exception.exception import CustomException
from typing import List

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
SUPABASE_API_URL = os.getenv("SUPABASE_API_URL")

# Create session with SQLModel
session_engine = create_engine(SUPABASE_API_URL, echo=True)

# Postgres connection string
db_url = f"postgresql://postgres:{DB_PASSWORD}@db.zrnnmetvtfteosglkrgw.supabase.co:5432/postgres"

# Select all the data
def get_all_network_logs() -> List[NetworkLogs]:
  try:
    with Session(session_engine) as session:
      statement = NetworkLogs.select()
      results = session.exec(statement)
      network = results.all()
      return network
  except Exception as e:
    raise CustomException(e, sys)