# ============================================================
# services/gemini_service.py - Gemini API Wrapper
# ============================================================
# This file handles ALL communication with the Gemini API.
# Every other service calls this file instead of calling
# the API directly. This is called the "Single Responsibility
# Principle" - one file, one job.
# ============================================================

from google import genai          # New official Gemini SDK
from config import Config         # Our app settings

def call_gemini(prompt):
    """
    Sends a prompt to the Gemini API and returns the response text.

    This is the ONLY place in the entire project where we
    directly talk to the Gemini API. All 4 functions use this.

    Args:
        prompt (str): The complete prompt string to send

    Returns:
        str: The AI's response text, or an error message
    """

    try:
        # Step 1: Create a Gemini client using our API key
        client = genai.Client(api_key=Config.GEMINI_API_KEY)

        # Step 2: Send the prompt and get a response
        response = client.models.generate_content(
            model=Config.GEMINI_MODEL,
            contents=prompt
        )

        # Step 3: Extract and return just the text
        return response.text

    except Exception as e:
        # If anything goes wrong, return a friendly error message
        # instead of crashing the whole application
        error_message = str(e)

        # Handle specific known errors with friendly messages
        if "429" in error_message:
            return "⚠️ API rate limit reached. Please wait a moment and try again."
        elif "API_KEY" in error_message or "401" in error_message:
            return "⚠️ Invalid API key. Please check your .env file."
        elif "404" in error_message:
            return "⚠️ Model not found. Please check the model name in config.py."
        else:
            return f"⚠️ Something went wrong: {error_message}"