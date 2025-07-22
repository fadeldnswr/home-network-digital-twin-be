'''
Modules to handle utility functions for the application.
This module includes functions for data validation, configuration management,
'''

from supabase import Client, create_client
from src.exception.exception import CustomException

import sys

# Define function to create a Supabase client
def create_supabase_client(url: str, key: str) -> Client:
  '''
  Function to create a Supabase client.
  Args:
    url (str): The Supabase URL.
    key (str): The Supabase API key.
  '''
  try:
    # Check if URL and key are not provided
    if not url or not key:
      print("Supabase URL or API key is not provided.")
    else:
      supabase: Client = create_client(url, key)
      return supabase
  except Exception as e:
    raise CustomException(e, sys)