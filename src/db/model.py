'''
Supabase database models.
This module defines the database models used in the Supabase backend for the home network digital twin project.
It includes the necessary imports and model definitions for interacting with the Supabase database.
'''

from sqlmodel import SQLModel, Field
from datetime import datetime

# Create table models
class NetworkLogs(SQLModel, table=True):
  id: str = Field(primary_key=True, nullable=False)
  time: datetime = Field(default_factory=datetime.now, nullable=False)
  jitter_ms: float = Field(nullable=False)
  latency_ms: float = Field(nullable=False)
  packet_loss: float = Field(nullable=False)
  download_speed_mbps: float = Field(nullable=False)
  upload_speed_mbps: float = Field(nullable=False)
  device_count: int = Field(nullable=False)