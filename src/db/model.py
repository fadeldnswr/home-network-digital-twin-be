'''
Supabase database models.
This module defines the database models used in the Supabase backend for the home network digital twin project.
It includes the necessary imports and model definitions for interacting with the Supabase database.
'''

from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import uuid4, UUID

# Create table models for real data
class NetworkData(SQLModel, table=True):
  __tablename__ = "network_data" # Override the default table name
  
  id: UUID = Field(default_factory=uuid4, primary_key=True)
  time: datetime = Field(default_factory=datetime.now, nullable=False)
  latency_ms: float = Field(nullable=False)
  jitter_ms: float = Field(nullable=False)
  packet_loss: float = Field(nullable=False)
  rssi_dbm: int = Field(nullable=False)
  interface: str = Field(nullable=False)
  download_mbps: float = Field(nullable=False)
  upload_mbps: float = Field(nullable=False)
  cpu_usage: float = Field(nullable=False)
  ram_usage: float = Field(nullable=False)
  device_count: int = Field(nullable=False)
  temp: float = Field(nullable=False)

# Create table models for digital twin data
class NetworkDataSimulation(SQLModel, table=True):
  __tablename__ = "network_data_simulation" # Override the default table name
  
  id: UUID = Field(default_factory=uuid4, primary_key=True)
  time: datetime = Field(default_factory=datetime.now, nullable=False)
  latency_ms: float = Field(nullable=False)
  jitter_ms: float = Field(nullable=False)
  packet_loss: float = Field(nullable=False)
  rssi_dbm: int = Field(nullable=False)
  interface: str = Field(nullable=False)
  download_mbps: float = Field(nullable=False)
  upload_mbps: float = Field(nullable=False)
  cpu_usage: float = Field(nullable=False)
  ram_usage: float = Field(nullable=False)
  device_count: int = Field(nullable=False)
  temp: float = Field(nullable=False)