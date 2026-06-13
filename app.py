# ============================================================
# app.py - Main Flask Application Entry Point
# ============================================================
# This is the file you run to start the entire application.
# It creates the Flask app, registers all routes (blueprints),
# and starts the development server.
# Command to run: python app.py
# ============================================================

from flask import Flask, render_template
from config import Config

# Import all route blueprints
from routes.qa_routes        import qa_bp
from routes.summarize_routes import summarize_bp
from routes.generate_routes  import generate_bp
from routes.advisor_routes   import advisor_bp

# ============================================================
# Step 1: Create the Flask application instance
# ============================================================
app = Flask(__name__)
app.config.from_object(Config)   # Load settings from config.py


# ============================================================
# Step 2: Register all Blueprints
# Each blueprint handles one function's routes.
# ============================================================
app.register_blueprint(qa_bp)
app.register_blueprint(summarize_bp)
app.register_blueprint(generate_bp)
app.register_blueprint(advisor_bp)


# ============================================================
# Step 3: Home Page Route
# ============================================================
@app.route("/")
def home():
    """
    GET /
    Renders the home/landing page of the AI Assistant.
    """
    return render_template("index.html")


# ============================================================
# Step 4: Run the application
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("  AI Assistant is starting...")
    print("  Open your browser: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=Config.DEBUG)