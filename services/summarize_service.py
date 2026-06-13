# ============================================================
# services/summarize_service.py - Text Summarization Service
# ============================================================
# Handles business logic for Function 2: Text Summarization
# ============================================================

from prompts.summarize_prompts import get_summarize_prompt
from services.gemini_service import call_gemini

def summarize_text(text, style="bullet"):
    """
    Takes a block of text, builds a summarization prompt,
    calls Gemini, and returns the summary.

    Args:
        text (str): The text to summarize (from user)
        style (str): "quick", "bullet", or "academic"
                     Default is "bullet" - most useful format

    Returns:
        dict: {
            "success": True/False,
            "response": "summary text",
            "prompt_style": style,
            "function": "summarize",
            "word_count": original word count
        }
    """

    # Step 1: Validate - text must not be empty
    if not text or text.strip() == "":
        return {
            "success": False,
            "response": "Please enter some text to summarize.",
            "prompt_style": style,
            "function": "summarize",
            "word_count": 0
        }

    # Step 2: Check minimum length - summarizing 5 words makes no sense
    word_count = len(text.strip().split())
    if word_count < 20:
        return {
            "success": False,
            "response": "Please enter at least 20 words for a meaningful summary.",
            "prompt_style": style,
            "function": "summarize",
            "word_count": word_count
        }

    # Step 3: Build prompt
    prompt = get_summarize_prompt(style, text.strip())

    # Step 4: Call Gemini
    response = call_gemini(prompt)

    # Step 5: Return result with original word count (useful for UI)
    return {
        "success": True,
        "response": response,
        "prompt_style": style,
        "function": "summarize",
        "word_count": word_count
    }