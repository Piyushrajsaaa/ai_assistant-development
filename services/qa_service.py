# ============================================================
# services/qa_service.py - Question Answering Service
# ============================================================
# Handles the business logic for Function 1: Question Answering
# Connects the QA prompts with the Gemini API call.
# ============================================================

from prompts.qa_prompts import get_qa_prompt      # Our prompt templates
from services.gemini_service import call_gemini    # Our Gemini wrapper

def answer_question(question, style="educational"):
    """
    Takes a user's question, builds the right prompt,
    calls Gemini, and returns the answer.

    Args:
        question (str): The question from the user
        style (str): Prompt style - "simple", "educational", "detailed"
                     Default is "educational" for best results

    Returns:
        dict: {
            "success": True/False,
            "response": "AI answer text",
            "prompt_style": "which style was used",
            "function": "qa"
        }
    """

    # Step 1: Validate input - don't send empty questions
    if not question or question.strip() == "":
        return {
            "success": False,
            "response": "Please enter a question.",
            "prompt_style": style,
            "function": "qa"
        }

    # Step 2: Build the prompt using our template
    prompt = get_qa_prompt(style, question.strip())

    # Step 3: Call Gemini and get the answer
    response = call_gemini(prompt)

    # Step 4: Return structured result
    return {
        "success": True,
        "response": response,
        "prompt_style": style,
        "function": "qa"
    }