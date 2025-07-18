'''
Main script to run the application.
'''

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
  title="Internet of Things and Digital Twin API",
  description="API for creating simulation and prediction to Internet of Things data with Digital Twin concepts.",
  version="0.1.0",
  contact={
    "name": "Fadel Achmad Daniswara",
    "email": "daniswarafadel@gmail.com"
  }
)

# Define CORS middleware to allow cross-origin requests
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"], 
  allow_credentials=True,
  allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
  allow_headers=["*"],  # Allow all headers
)

# Define the API routers

# Define a simple root endpoint
@app.get("/")
async def first_simple_route():
  '''
  Root endpoint to check if the API is running.
  '''
  try:
    return  {
      "message": "Welcome to the Internet of Things and Digital Twin API!",
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))