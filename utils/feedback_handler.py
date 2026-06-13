# ============================================================
# utils/feedback_handler.py - Feedback Storage Utility
# ============================================================
# Saves and reads user feedback from a local JSON file.
# No database needed - JSON file is perfect for this project.
# ============================================================

import json          # Built-in Python module for JSON
import os            # For file path operations
from datetime import datetime   # To timestamp each feedback
from config import Config       # For feedback file path

def save_feedback(function_name, user_input, ai_response, was_helpful):
    """
    Saves one feedback entry to the feedback.json file.

    Args:
        function_name (str): Which function was used (qa, summarize, etc.)
        user_input    (str): What the user typed
        ai_response   (str): What the AI responded
        was_helpful   (bool): True if user clicked Yes, False for No

    Returns:
        bool: True if saved successfully, False if error
    """

    # Build one feedback record as a dictionary
    feedback_entry = {
        "timestamp"    : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "function"     : function_name,
        "user_input"   : user_input[:200],    # Limit to 200 chars
        "ai_response"  : ai_response[:300],   # Limit to 300 chars
        "was_helpful"  : was_helpful
    }

    try:
        # Step 1: Load existing feedback if file exists
        existing_feedback = []
        if os.path.exists(Config.FEEDBACK_FILE):
            with open(Config.FEEDBACK_FILE, "r") as f:
                existing_feedback = json.load(f)

        # Step 2: Add the new entry
        existing_feedback.append(feedback_entry)

        # Step 3: Write everything back to the file
        with open(Config.FEEDBACK_FILE, "w") as f:
            json.dump(existing_feedback, f, indent=4)

        return True

    except Exception as e:
        print(f"Error saving feedback: {e}")
        return False


def get_all_feedback():
    """
    Reads and returns all feedback from the JSON file.

    Returns:
        list: List of all feedback entries, empty list if none
    """
    try:
        if os.path.exists(Config.FEEDBACK_FILE):
            with open(Config.FEEDBACK_FILE, "r") as f:
                return json.load(f)
        return []
    except Exception:
        return []


def get_feedback_stats():
    """
    Returns simple statistics about collected feedback.
    Useful for the UI dashboard and documentation.

    Returns:
        dict: {
            "total": total feedback count,
            "helpful": count of helpful responses,
            "not_helpful": count of not helpful,
            "helpful_percent": percentage helpful
        }
    """
    all_feedback = get_all_feedback()
    total = len(all_feedback)

    if total == 0:
        return {
            "total": 0,
            "helpful": 0,
            "not_helpful": 0,
            "helpful_percent": 0
        }

    helpful = sum(1 for f in all_feedback if f.get("was_helpful") == True)
    not_helpful = total - helpful

    return {
        "total": total,
        "helpful": helpful,
        "not_helpful": not_helpful,
        "helpful_percent": round((helpful / total) * 100, 1)
    }