# ============================================================
# services/generate_service.py - Content Generation Service
# ============================================================
# Handles business logic for Function 3: Content Generation
# ============================================================

from prompts.generate_prompts import get_generate_prompt
from services.gemini_service import call_gemini

# Valid content types the user can request
VALID_CONTENT_TYPES = ["story", "poem", "essay", "idea"]

def generate_content(topic, content_type="story", style="detailed"):
    """
    Generates creative content based on user topic and type.

    Args:
        topic (str): The topic or theme (e.g., "a robot falling in love")
        content_type (str): "story", "poem", "essay", or "idea"
        style (str): "simple", "detailed", or "structured"

    Returns:
        dict: {
            "success": True/False,
            "response": "generated content",
            "content_type": type used,
            "prompt_style": style used,
            "function": "generate"
        }
    """

    # Step 1: Validate topic
    if not topic or topic.strip() == "":
        return {
            "success": False,
            "response": "Please enter a topic or theme.",
            "content_type": content_type,
            "prompt_style": style,
            "function": "generate"
        }

    # Step 2: Validate content type
    if content_type not in VALID_CONTENT_TYPES:
        content_type = "story"   # Default to story if invalid

    # Step 3: Build prompt
    prompt = get_generate_prompt(content_type, style, topic.strip())

    # Step 4: Call Gemini
    response = call_gemini(prompt)

    # Step 5: Return result
    return {
        "success": True,
        "response": response,
        "content_type": content_type,
        "prompt_style": style,
        "function": "generate"
    }