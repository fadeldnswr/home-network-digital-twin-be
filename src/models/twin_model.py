'''
Twin model module that defines the structure and behavior of a digital twin in the context of home network monitoring.
This module includes methods for initializing the twin, updating its state, and retrieving its properties.
'''

import simpy
import sys
import random
import pandas as pd

from src.exception.exception import CustomException
from src.logging.logging import logging
from datetime import datetime

# Define the agregate twin model class
class TwinModel:
  def __init__(
    self, env: simpy.Environment, rssi_dbm, device_count, cpu_usage,
    memory_usage, log_output):
    self.env = env
    self.rssi_dbm = rssi_dbm
    self.device_count = device_count
    self.cpu_usage = cpu_usage
    self.memory_usage = memory_usage
    self.log_output = log_output
    self.process = env.process(self.run_simulation())
  
  def run_simulation(self):
    '''
    Run the simulation process for the twin model.
    '''
    try:
      while True:
        latency = self.calculate_latency()
        jitter = random.gauss(1, 6)
        packet_loss = self.calculate_packet_loss()
        
        # Log the output
        self.log_output.append({
          "timestamp": self.env.now,
          "rssi_dbm": self.rssi_dbm,
          "device_count": self.device_count,
          "cpu_usage": self.cpu_usage,
          "memory_usage": self.memory_usage,
          "jitter_ms": jitter,
          "latency_ms": latency,
          "packet_loss_percent": packet_loss
        })
        yield self.env.timeout(300)
    except Exception as e:
      raise CustomException(e, sys)
  
  def calculate_latency(self):
    '''
    Calculate the latency based on the RSSI value.
    '''
    base_latency = 15 # Base latency in milliseconds
    load_penalty = self.device_count * 1.2
    signal_penalty = max(0, -self.rssi_dbm - 50) * 0.5
    cpu_penalty = self.cpu_usage * 0.2
    return base_latency + load_penalty + signal_penalty + cpu_penalty
  
  def calculate_packet_loss(self):
    '''
    Calculate the packet loss based on the RSSI value.
    '''
    return min(0.005 * self.device_count + max(0, -self.rssi_dbm - 60) * 0.03, 1.0)

# Define function to run the agregate twin model simulation
def run_aggregate_simulation(
  duration_minutes:int=100, rssi_dbm:int=-30, 
  device_count:int=6, cpu_usage:float=40.0, memory_usage:float=70.0
) -> pd.DataFrame:
  '''
  Function to run the aggregate twin model simulation.
  '''
  try:
    env = simpy.Environment()
    logs = []
    TwinModel(
      env=env, rssi_dbm=rssi_dbm,
      device_count=device_count, cpu_usage=cpu_usage,
      log_output=logs, memory_usage=memory_usage
    )
    env.run(until=duration_minutes * 60)
    return pd.DataFrame(logs)
  except Exception as e:
    raise CustomException(e, sys)


# Run the simulation process
if __name__ == "__main__":
  try:
    data = run_aggregate_simulation()
    print(data.head())
  except Exception as e:
    raise CustomException(e, sys)