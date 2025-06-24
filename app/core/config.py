import os
import logging
from pydantic import BaseModel, validator
from dotenv import load_dotenv
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

class settings(BaseModel):
    # Project settings
    PROJECT_NAME: str = "AI Based LMS"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "A LMS that uses AI to generate course content and provide personalized learning experiences."
    
    # API settings
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    GROQ_API_URL: str = os.getenv("GROQ_API_URL", "")
    LLM_MODEL: str = "llama-3.3-70b-versatile"  # Updated to a more capable model

settings = settings()