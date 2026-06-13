# ============================================================
# routes/summarize_routes.py - Summarization Routes
# ============================================================

from flask import Blueprint, request, jsonify, render_template
from services.summarize_service import summarize_text
from utils.feedback_handler import save_feedback

summarize_bp = Blueprint("summarize", __name__)


@summarize_bp.route("/summarize")
def summarize_page():
    """GET /summarize — Renders the Summarization HTML page."""
    return render_template("summarize.html")


@summarize_bp.route("/summarize/run", methods=["POST"])
def summarize_run():
    """
    POST /summarize/run
    Receives text + style, returns summary as JSON.

    Expected JSON body:
    {
        "text": "Long paragraph here...",
        "style": "bullet"
    }
    """

    data = request.get_json()
    text  = data.get("text", "").strip()
    style = data.get("style", "bullet")

    result = summarize_text(text, style)

    return jsonify(result)


@summarize_bp.route("/summarize/feedback", methods=["POST"])
def summarize_feedback():
    """POST /summarize/feedback — Saves summarization feedback."""

    data = request.get_json()

    saved = save_feedback(
        function_name = "summarize",
        user_input    = data.get("user_input", ""),
        ai_response   = data.get("ai_response", ""),
        was_helpful   = data.get("was_helpful", False)
    )

    return jsonify({
        "success": saved,
        "message": "Thank you for your feedback!" if saved else "Could not save feedback."
    })