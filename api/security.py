import os

from dotenv import load_dotenv
from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

# Load environment variables from .env file
load_dotenv()

API_KEY_NAME = "X-API-KEY"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

SERVER_API_KEY = os.getenv("SERVER_API_KEY")


def get_api_key(api_key: str = Security(api_key_header)):
    """Dependency to validate the API key from the X-API-KEY header."""
    if api_key != SERVER_API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    return api_key
