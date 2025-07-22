'''
Data loading module for the home network digital twin project.
This module handles the loading of data into the system, including data validation and transformation.
Data will be loaded to Supabase after Digital Twin simulation has been created.
'''

import pandas as pd
import os
import sys

from src.exception.exception import CustomException
from src.logging.logging import logging
from typing import List, Dict
from src.utils.utils import create_supabase_client

# Define class for data loading
class DataLoad:
  def __init__(self):
    pass
  
  def load_data_to_supabase(self, data:pd.DataFrame, table_name:str) -> None:
    try:
      pass
    except Exception as e:
      raise CustomException(e, sys)