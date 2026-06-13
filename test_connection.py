# ============================================================
# test_connection.py - Test Gemini API Connection (New SDK)
# ============================================================

from google import genai          # New SDK import
from config import Config

def test_gemini_connection():
    print("=" * 50)
    print("  Testing Gemini API Connection...")
    print("=" * 50)

    if not Config.GEMINI_API_KEY or Config.GEMINI_API_KEY == "your_gemini_api_key_here":
        print("ERROR: Please set your GEMINI_API_KEY in the .env file.")
        return

    try:
        # Step 1: Create client with API key
        client = genai.Client(api_key=Config.GEMINI_API_KEY)

        # Step 2: Send test prompt
        response = client.models.generate_content(
            model=Config.GEMINI_MODEL,
            contents="Say exactly: Hello! Gemini AI is ready to assist."
        )

        # Step 3: Print result
        print("Connection Successful!")
        print(f"Model used : {Config.GEMINI_MODEL}")
        print(f"Response   : {response.text}")
        print("=" * 50)
        print("Setup COMPLETE. Ready to build!")

    except Exception as e:
        print(f"Connection FAILED!")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_gemini_connection()