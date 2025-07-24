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
from src.db.utils import get_all_network_logs

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
    self.data_logs = None
  
  def extract_data_from_supabase(self) -> pd.DataFrame:
    '''
    Extract data from a specified Supabase table.
    Args:
      table_name (str): The name of the table to extract data from.
    Returns:
      list: A list of dictionaries containing the extracted data.
    '''
    try:
      # Define the response from Supabase
      self.data_logs = get_all_network_logs() # Fetch all network logs from the database
      if not self.data_logs:
        raise CustomException(e, sys)
      
      # Convert the data to pandas DataFrame
      df = pd.DataFrame([log.model_dump() for log in self.data_logs])
      return df
    except Exception as e:
      raise CustomException(e, sys)

# Run the data extraction if this script is executed directly
if __name__ == "__main__":
  try:
    data_extraction = DataExtraction()
    data = data_extraction.extract_data_from_supabase()
    print(data.head())  # Print the first few rows of the extracted data
  except Exception as e:
    raise CustomException(e, sys)