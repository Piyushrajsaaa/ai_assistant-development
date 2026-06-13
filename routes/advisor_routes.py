# ============================================================
# routes/advisor_routes.py - Study Advisor Routes
# ============================================================

from flask import Blueprint, request, jsonify, render_template
from services.advisor_service import get_study_advice
from utils.feedback_handler import save_feedback

advisor_bp = Blueprint("advisor", __name__)


@advisor_bp.route("/advisor")
def advisor_page():
    """GET /advisor — Renders the Study Advisor HTML page."""
    return render_template("advisor.html")


@advisor_bp.route("/advisor/run", methods=["POST"])
def advisor_run():
    """
    POST /advisor/run
    Receives query + style, returns study advice as JSON.

    Expected JSON body:
    {
        "query": "How to prepare for DSA interviews?",
        "style": "roadmap"
    }
    """

    data  = request.get_json()
    query = data.get("query", "").strip()
    style = data.get("style", "roadmap")

    result = get_study_advice(query, style)

    return jsonify(result)


@advisor_bp.route("/advisor/feedback", methods=["POST"])
def advisor_feedback():
    """POST /advisor/feedback — Saves advisor feedback."""

    data = request.get_json()

    saved = save_feedback(
        function_name = "advisor",
        user_input    = data.get("user_input", ""),
        ai_response   = data.get("ai_response", ""),
        was_helpful   = data.get("was_helpful", False)
    )

    return jsonify({
        "success": saved,
        "message": "Thank you for your feedback!" if saved else "Could not save feedback."
    })