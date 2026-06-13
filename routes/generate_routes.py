# ============================================================
# routes/generate_routes.py - Content Generation Routes
# ============================================================

from flask import Blueprint, request, jsonify, render_template
from services.generate_service import generate_content
from utils.feedback_handler import save_feedback

generate_bp = Blueprint("generate", __name__)


@generate_bp.route("/generate")
def generate_page():
    """GET /generate — Renders the Content Generation HTML page."""
    return render_template("generate.html")


@generate_bp.route("/generate/run", methods=["POST"])
def generate_run():
    """
    POST /generate/run
    Receives topic + content_type + style, returns generated content.

    Expected JSON body:
    {
        "topic": "a dragon who learns to code",
        "content_type": "story",
        "style": "detailed"
    }
    """

    data         = request.get_json()
    topic        = data.get("topic", "").strip()
    content_type = data.get("content_type", "story")
    style        = data.get("style", "detailed")

    result = generate_content(topic, content_type, style)

    return jsonify(result)


@generate_bp.route("/generate/feedback", methods=["POST"])
def generate_feedback():
    """POST /generate/feedback — Saves generation feedback."""

    data = request.get_json()

    saved = save_feedback(
        function_name = "generate",
        user_input    = data.get("user_input", ""),
        ai_response   = data.get("ai_response", ""),
        was_helpful   = data.get("was_helpful", False)
    )

    return jsonify({
        "success": saved,
        "message": "Thank you for your feedback!" if saved else "Could not save feedback."
    })