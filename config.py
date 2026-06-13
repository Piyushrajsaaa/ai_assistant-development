# ============================================================
# config.py - Central Configuration File
# ============================================================
# All app-wide settings live here. Import this wherever needed.
# ============================================================

import os
from dotenv import load_dotenv

# Load variables from .env file into the environment
load_dotenv()

class Config:
    """
    Holds all application-wide settings.
    Any file can do: from config import Config
    """

    # Gemini API Key - loaded from .env file
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

    # Which Gemini model to use (free-tier friendly)
    GEMINI_MODEL = "gemini-2.5-flash"

    # Flask secret key (needed for sessions)
    SECRET_KEY = os.getenv("SECRET_KEY", "ai-assistant-secret-2024")

    # Show detailed errors during development
    DEBUG = True

    # Where to store user feedback
    FEEDBACK_FILE = "feedback.json"

    # AI response settings
    MAX_OUTPUT_TOKENS = 1024  # Max response length
    TEMPERATURE = 0.7         # 0=focused, 1=creative