# ============================================================
# services/advisor_service.py - Study Advisor Service
# ============================================================
# Handles business logic for Function 4: Study Advisor
# ============================================================

from prompts.advisor_prompts import get_advisor_prompt
from services.gemini_service import call_gemini

def get_study_advice(query, style="roadmap"):
    """
    Takes a study-related query and returns personalized advice.

    Args:
        query (str): What the user wants to learn/study
        style (str): "quick", "roadmap", or "expert"
                     Default is "roadmap" - most structured

    Returns:
        dict: {
            "success": True/False,
            "response": "advice text",
            "prompt_style": style,
            "function": "advisor"
        }
    """

    # Step 1: Validate input
    if not query or query.strip() == "":
        return {
            "success": False,
            "response": "Please enter a topic you want study advice for.",
            "prompt_style": style,
            "function": "advisor"
        }

    # Step 2: Build prompt
    prompt = get_advisor_prompt(style, query.strip())

    # Step 3: Call Gemini
    response = call_gemini(prompt)

    # Step 4: Return result
    return {
        "success": True,
        "response": response,
        "prompt_style": style,
        "function": "advisor"
    }