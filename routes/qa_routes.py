# ============================================================
# routes/qa_routes.py - Question Answering Routes
# ============================================================
# Defines URL endpoints for the QA function.
# Blueprint = a mini Flask app we register in app.py
# ============================================================

from flask import Blueprint, request, jsonify, render_template
from services.qa_service import answer_question
from utils.feedback_handler import save_feedback

# Create a Blueprint named "qa"
# All routes here will be prefixed with /qa
qa_bp = Blueprint("qa", __name__)


@qa_bp.route("/qa")
def qa_page():
    """
    GET /qa
    Renders the Question Answering HTML page.
    """
    return render_template("qa.html")


@qa_bp.route("/qa/answer", methods=["POST"])
def qa_answer():
    """
    POST /qa/answer
    Receives question + style, returns AI answer as JSON.

    Expected JSON body:
    {
        "question": "What is machine learning?",
        "style": "educational"
    }

    Returns JSON:
    {
        "success": true,
        "response": "Machine learning is...",
        "prompt_style": "educational"
    }
    """

    # Step 1: Get data from the request body
    data = request.get_json()

    # Step 2: Extract values (use defaults if not provided)
    question = data.get("question", "").strip()
    style = data.get("style", "educational")

    # Step 3: Call the service
    result = answer_question(question, style)

    # Step 4: Return JSON response to the frontend
    return jsonify(result)


@qa_bp.route("/qa/feedback", methods=["POST"])
def qa_feedback():
    """
    POST /qa/feedback
    Saves user feedback for a QA response.

    Expected JSON body:
    {
        "user_input": "What is AI?",
        "ai_response": "AI is...",
        "was_helpful": true
    }
    """

    data = request.get_json()

    saved = save_feedback(
        function_name = "qa",
        user_input    = data.get("user_input", ""),
        ai_response   = data.get("ai_response", ""),
        was_helpful   = data.get("was_helpful", False)
    )

    return jsonify({
        "success": saved,
        "message": "Thank you for your feedback!" if saved else "Could not save feedback."
    })