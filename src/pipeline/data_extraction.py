'''
Data extraction module for the home network digital twin project.
This module handles the extraction of data from various sources, including Supabase,
and processes it for use in the simulation.
'''

import sys
import os
import supabase
import pandas as pd

from src.utils.utils import create_supabase_client
from src.exception.exception import CustomException
from src.logging.logging import logging
from typing import List, Dict

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

SUPABASE_API_URL = os.getenv("SUPABASE_API_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

# Check the conditions for Supabase API URL and key
if not SUPABASE_API_URL or not SUPABASE_API_KEY:
  print("Supabase API URL or key is not set in the environment variables.") # Print error message
else:
  supabase = create_supabase_client(SUPABASE_API_URL, SUPABASE_API_KEY) # Create a Supabase client

# Define class for data extraction
class DataExtraction:
  def __init__(self):
    self.supabase = supabase
    if not self.supabase:
      print("Failed to create Supabase client. Check your environment variables.")
  
  def extract_data_from_supabase(self, table_name:str) -> pd.DataFrame:
    '''
    Extract data from a specified Supabase table.
    Args:
      table_name (str): The name of the table to extract data from.
    Returns:
      list: A list of dictionaries containing the extracted data.
    '''
    try:
      # Define the response from Supabase
      response = self.supabase.table(table_name).select("*").execute()
      
      # Convert the response data to a DataFrame
      if response.data:
        data = pd.DataFrame(response.data)
        return data
      else:
        print(f"No data found in the table '{table_name}'.")
        return pd.DataFrame()
    except Exception as e:
      raise CustomException(e, sys)

# Run the data extraction if this script is executed directly
if __name__ == "__main__":
  try:
    data_extraction = DataExtraction()
    data = data_extraction.extract_data_from_supabase("network_data")
    print(data.head())  # Print the first few rows of the extracted data
  except Exception as e:
    raise CustomException(e, sys)